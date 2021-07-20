import pandas as pd
import numpy as np
import h5py
import argparse
import unit_conversions as uc


def convert(func, x):
    '''Converts numpy arrays in place'''
    for i in range(0, len(x)):
        x[i] = func(x[i])


def rem_to_microsv(x):
    '''Converts rem to microsv'''
    return uc.micro(uc.rem_to_sv(x))


def microsv_to_rem(x):
    '''Converts microsv to rem'''
    return uc.mega(uc.sv_to_rem(x))


def psv_cm2_to_microsv_hour(x):
    '''Converts psv cm2 to microsv/hour per n/cm2/s'''
    return uc.mega(3600 * x)


def microsv_hour_to_psv_cm2(x):
    '''Converts microsv/hour per n/cm2/s to psv cm2'''
    return uc.micro(x / 3600)


def psv_cm2_to_rem_hour(x):
    '''Converts psv cm2 to rem/hour per n/cm2/s'''
    return uc.tera(3600 * x) * 100


def rem_hour_to_psv_cm2(x):
    '''Converts rem/hour per n/cm2/s to psv cm2'''
    return uc.pico(x / 3600) / 100


def read_hdf5(file, edit_type):
    '''Opens a hdf5 file for reading'''
    return h5py.File(file, edit_type)


def check_e_units(e_units, dcf_units, dose):
    if e_units == 'pSv cm2':
        if dcf_units == 1:
            convert(psv_cm2_to_microsv_hour, dose)
        elif dcf_units == 2:
            convert(psv_cm2_to_rem_hour, dose)
        elif dcf_units == 3:
            pass
        else:
            raise ValueError('Invalid output unit! See -h for valid units.')
    elif e_units == 'rem/h per n/cm2/s':
        if dcf_units == 1:
            convert(rem_to_microsv, dose)
        elif dcf_units == 2:
            pass
        elif dcf_units == 3:
            convert(rem_hour_to_psv_cm2, dose)
        else:
            raise ValueError('Invalid output unit! See -h for valid units.')
    elif e_units == 'microSv/h per n/cm2/s':
        if dcf_units == 1:
            pass
        elif dcf_units == 2:
            convert(microsv_to_rem, dose)
        elif dcf_units == 3:
            convert(microsv_hour_to_psv_cm2, dose)
        else:
            raise ValueError('Invalid output unit! See -h for valid units.')
    else:
        raise ValueError('Your DCF units are not accepted in this program. See -h for accepted units.')


def check(file, group, dataset, orientation, dcf_units):
    '''Checks to see if the requested data exists / is valid and returns it in the requested units'''
    if group in list(file.keys()):
        path = '/' + group
        e_units = file.get(path).attrs['dcf_units']
        if dataset in list(file.get(path).keys()):
            path = '/' + group + '/' + dataset 
            if orientation in list(file.get(path).keys()):
                path = '/' + group + '/' + dataset + '/' + orientation
                data = pd.DataFrame(file.get(path), columns=['E', 'DCF']).reset_index(drop=True)
                dose = np.array(data['DCF'])
                check_e_units(e_units, dcf_units, dose)
                data['DCF'] = dose
            else:
                raise ValueError('Invalid orientation! Valid orientations for this dataset are: ', file.get(path).keys())
        else:
            raise ValueError('Invalid dataset! Valid datasets for this group are: ', file.get(path).keys())
    else:
        raise ValueError('Invalid group! Valid groups are: ', file.keys())
    
    return data


def output_mcnp_format(file, group, dataset, orientation, data, dcf_units):
    '''Outputs the data in a format suitable for use in MCNP'''
    new_energy = []
    new_energy_line = '   '
    for x in data.iloc[:, 0]:
        if len(new_energy_line) < 80 and len(new_energy_line + ' ' + str(('{:.2e}').format(x))) < 80:
            new_energy_line += ' ' + str(('{:.2e}').format(x))
        if len(new_energy_line) >= 80 or len(new_energy_line + ' ' + str(('{:.2e}').format(x))) > 80:
            new_energy.append(new_energy_line)
            new_energy_line = '   '
    new_dcf = []
    new_dcf_line = '   '
    for x in data.iloc[:, 1]:
        if len(new_dcf_line) < 80 and len(new_dcf_line + ' ' + str(('{:.2e}').format(x))) < 80:
            new_dcf_line += ' ' + str(('{:.2e}').format(x))
        if len(new_dcf_line) >= 80 or len(new_dcf_line + ' ' + str(('{:.2e}').format(x))) > 80:
            new_dcf.append(new_dcf_line)
            new_dcf_line = '   '
    with open('{}_{}_{}_mcnp.txt'.format(group, dataset, orientation), 'w') as new_f:
        new_f.write('DEXX $ Energy ({})\n'.format(file.get('/'+group).attrs['energy_units']))
        new_f.write('\n'.join(new_energy))
        new_f.write('\n')
        new_f.write('DFXX $ DCF ({})\n'.format(dcf_units))
        new_f.write('\n'.join(new_dcf))


def plot(data, xdata, ydata, group, dcf_units):
    '''Plots the data (if requested)'''
    data.plot(kind='line', x=xdata, y=ydata, xlabel=('E ({})'.format(file.get('/'+group).attrs['energy_units'])), ylabel=('DCF ({})'.format(dcf_units)), legend=False, logx=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('group', type=str, help='The group you would like to retrieve data from. Enter without apostrophes.')
    parser.add_argument('dataset', type=str, help='The dataset you would like to retrieve data from. Enter without apostrophes.')
    parser.add_argument('-ot', '--orientation', type=str, default='ISO', metavar='', help='The orientation of the particle beam. Default: ISO.')
    parser.add_argument('-pt', '--plot_true', dest='plot_true_false', action='store_true', help='Will plot the data.')
    parser.add_argument('-pf', '--plot_false', dest='plot_true_false', action='store_false', help='Will not plot the data.')
    parser.set_defaults(plot_true_false=True)
    parser.add_argument('-ou', '--output_dcf_units', type=int, default=1, metavar='', help='The index of your desired output DCF units. 1 = microSv/h per n/cm2/s, 2 = rem/h per n/cm2/s, 3 = pSv cm2')
    parser.add_argument('-f', '--filename', type=str, metavar='', default='DCFfile.h5', help='The name of the hdf5 file you would like to read from. Please include .h5 at the end.')
    parser.add_argument('-o', '--output', type=str, metavar='', default='MCNP', help='The type of file you would like to output to. Accepted types are MCNP.')
    args = parser.parse_args()
    args.group = args.group.upper()
    args.dataset = args.dataset.lower()
    args.orientation = args.orientation.upper()
    
    # Using numbers as reduces risk of typos
    if args.output_dcf_units == 1:
        output_dcf_units = 'microSv/h per n/cm2/s'
    elif args.output_dcf_units == 2:
        output_dcf_units = 'rem/h per n/cm2/s'
    elif args.output_dcf_units == 3:
        output_dcf_units = 'pSv cm2'
        
    if args.output != 'MCNP':
        raise ValueError('Output file format not yet supported!')
    
    file = read_hdf5(args.filename, 'r')
    
    data = check(file, args.group, args.dataset, args.orientation, args.output_dcf_units)
    pd.set_option('display.float_format', '{:.2e}'.format)
    
    output_mcnp_format(file, args.group, args.dataset, args.orientation, data, output_dcf_units)
    
    if args.plot_true_false == True:
        plot(data, data.columns[0], data.columns[1], args.group, output_dcf_units)
        print('Your data has been plotted and an MCNP friendly file has now been created! Look for {}_{}_{}_mcnp.txt'.format(args.group, args.dataset, args.orientation))
    elif args.plot_true_false == False:
        print('An MCNP friendly file has now been created! Look for {}_{}_{}_mcnp.txt'.format(args.group, args.dataset, args.orientation))
    
    file.close()
