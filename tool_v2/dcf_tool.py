import pandas as pd
import numpy as np
import h5py
import argparse
import unit_conversions as uc
import dcf_class


def convert(func, x):
    '''Converts numpy arrays in place'''
    for i in range(0, len(x)):
        x[i] = func(x[i])

    return x


def read_hdf5(file, path, group, organ, particle, orientation):
    '''Create a DCF class from hdf5 file'''
    data = pd.DataFrame(file.get(path), columns=['E', 'DCF']).reset_index(drop=True)
    e_units = file.get('/'+group+'/'+organ).attrs['energy_units']
    dcf_units = file.get('/'+group+'/'+organ).attrs['dcf_units']
    return dcf_class.DCF(group=group, organ=organ, particle=particle, orientation=orientation,
                         path=path, data=data, e_units=e_units, dcf_units=dcf_units)


def check_dcf_units(input_dcf_units, output_dcf_units, dcf_data):
    '''Checks that the DCF units are valid and converts them into the desired output unit'''
    if input_dcf_units == 'pSv cm2':
        if output_dcf_units == 'microSv/h per particle/cm2/s':
            convert(uc.psv_cm2_to_microsv_hour, dcf_data)
        elif output_dcf_units == 'rem/h per particle/cm2/s':
            convert(uc.psv_cm2_to_rem_hour, dcf_data)
        else:
            raise ValueError('Invalid output unit! See -h for valid units.')
    elif input_dcf_units == 'rem/h per particle/cm2/s':
        if output_dcf_units == 'microSv/h per particle/cm2/s':
            convert(uc.rem_to_microsv, dcf_data)
        elif output_dcf_units == 'pSv cm2':
            convert(uc.rem_hour_to_psv_cm2, dcf_data)
        else:
            raise ValueError('Invalid output unit! See -h for valid units.')
    elif input_dcf_units == 'microSv/h per particle/cm2/s':
        if output_dcf_units == 'rem/h per particle/cm2/s':
            convert(uc.microsv_to_rem, dcf_data)
        elif output_dcf_units == 'pSv cm2':
            convert(uc.microsv_hour_to_psv_cm2, dcf_data)
        else:
            raise ValueError('Invalid output unit! See -h for valid units.')
    else:
        raise ValueError('Your DCF units are not accepted in this program. See -h for accepted units.')


def check(file, group, organ, dataset, orientation, output_dcf_units):
    '''Checks to see if the requested data exists / is valid and returns it in the requested units'''
    if group in list(file.keys()):
        path = '/' + group
        if organ in list(file.get(path).keys()):
            path = path + '/' + organ
            if dataset in list(file.get(path).keys()):
                path = path + '/' + dataset
                if orientation in list(file.get(path).keys()):
                    path = path + '/' + orientation
                    dcf_object = read_hdf5(file, path, group, organ , dataset, orientation)
                    if dcf_object.dcf_units == output_dcf_units or dcf_object.dcf_units == 'pGy cm2':
                        pass
                    else:
                        dcf_data = np.array(dcf_object.data['DCF'])
                        check_dcf_units(dcf_object.dcf_units, output_dcf_units, dcf_data)
                        dcf_object.data['DCF'] = dcf_data
                        dcf_object.dcf_units = output_dcf_units
                else:
                    raise ValueError('Invalid orientation! Valid orientations for this dataset are: ',
                                     file.get(path).keys())
            else:
                raise ValueError('Invalid dataset! Valid datasets for this organ are: ',
                                 file.get(path).keys())
        else:
            raise ValueError('Invalid organ! Valid organs for this group are: ',
                             file.get(path).keys())
    else:
        raise ValueError('Invalid group! Valid groups are: ', file.keys())

    return dcf_object


def output_mcnp_format(dcf_class):
    '''Outputs the data in a format suitable for use in MCNP'''
    if dcf_class.e_units != 'MeV':
        raise ValueError('To output to MCNP format, please ensure that your energy column '
                         'has units of MeV!')
    new_energy = []
    new_energy_line = '   '
    for x in dcf_class.data.iloc[:, 0]:
        if len(new_energy_line) < 80 and len(new_energy_line + ' ' + str(('{:.2e}').format(x))) < 80:
            new_energy_line += ' ' + str(('{:.2e}').format(x))
        if len(new_energy_line) >= 80 or len(new_energy_line + ' ' + str(('{:.2e}').format(x))) > 80:
            new_energy.append(new_energy_line)
            new_energy_line = '   '
    new_dcf = []
    new_dcf_line = '   '
    for x in dcf_class.data.iloc[:, 1]:
        if len(new_dcf_line) < 80 and len(new_dcf_line + ' ' + str(('{:.2e}').format(x))) < 80:
            new_dcf_line += ' ' + str(('{:.2e}').format(x))
        if len(new_dcf_line) >= 80 or len(new_dcf_line + ' ' + str(('{:.2e}').format(x))) > 80:
            new_dcf.append(new_dcf_line)
            new_dcf_line = '   '
    with open('{}_{}_{}_{}_MCNP.txt'.format(dcf_class.group, dcf_class.organ, dcf_class.particle,
                                            dcf_class.orientation), 'w') as new_f:
        new_f.write('DEXX $ Energy ({})\n'.format(dcf_class.e_units))
        new_f.write('\n'.join(new_energy))
        new_f.write('\n')
        new_f.write('DFXX $ DCF ({})\n'.format(dcf_class.dcf_units))
        new_f.write('\n'.join(new_dcf))


def plot(data, xdata, ydata, energy_units, dcf_units):
    '''Plots the data (if requested)'''
    data.plot(kind='line', x=xdata, y=ydata, xlabel=('E ({})'.format(energy_units)),
              ylabel=('DCF ({})'.format(dcf_units)), legend=False, logx=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('group', type=str, help='The group you would like to retrieve data from. '
                        'Enter without apostrophes.')
    parser.add_argument('dataset', type=str,
                        help='The dataset you would like to retrieve data from. '
                        'Enter without apostrophes.')
    parser.add_argument('-org', '--organ', type=str, default='full_body', metavar='',
                        help='The organ you would like data for. Default: full_body.')
    parser.add_argument('-ot', '--orientation', type=str, default='ISO', metavar='',
                        help='The orientation of the particle beam. Default: ISO.')
    parser.add_argument('-pt', '--plot_true', dest='plot_true_false', action='store_true',
                        help='Will plot the data.')
    parser.add_argument('-pf', '--plot_false', dest='plot_true_false', action='store_false',
                        help='Will not plot the data.')
    parser.set_defaults(plot_true_false=True)
    parser.add_argument('-dcf', '--output_dcf_units', type=int, default=1, metavar='',
                        help='Currently only relevant for full_body data. '
                        'The index of your desired output DCF units. 1 = microSv/h per particle/cm2/s, '
                        '2 = rem/h per particle/cm2/s, 3 = pSv cm2')
    parser.add_argument('-f', '--filename', type=str, metavar='', default='DCFfile.h5',
                        help='The name of the hdf5 file you would like to read from. '
                        'Please include .h5 at the end.')
    parser.add_argument('-o', '--output', type=str, metavar='', default='MCNP',
                        help='The type of file you would like to output to. Accepted types: MCNP.')
    args = parser.parse_args()
    args.group = args.group.upper()
    args.organ = args.organ.lower()
    args.dataset = args.dataset.lower()
    args.orientation = args.orientation.upper()

    # Using numbers as reduces risk of typos
    if args.output_dcf_units == 1:
        output_dcf_units = 'microSv/h per particle/cm2/s'
    elif args.output_dcf_units == 2:
        output_dcf_units = 'rem/h per particle/cm2/s'
    elif args.output_dcf_units == 3:
        output_dcf_units = 'pSv cm2'
    else:
        raise ValueError('Output unit not yet supported!')

    if args.output != 'MCNP':
        raise ValueError('Output file format not yet supported!')

    file = h5py.File(args.filename, 'r')

    dcf_object = check(file, args.group, args.organ, args.dataset,
                       args.orientation, output_dcf_units)
    pd.set_option('display.float_format', '{:.2e}'.format)

    output_mcnp_format(dcf_object)

    if args.plot_true_false is True:
        plot(dcf_object.data, dcf_object.data.columns[0], dcf_object.data.columns[1],
             dcf_object.e_units, dcf_object.dcf_units)
        print('Your data has been plotted and an {} friendly file has now been created! '
              'Look for {}_{}_{}_{}_{}.txt'.format(args.output, args.group, args.organ,
                                                   args.dataset, args.orientation, args.output))
    elif args.plot_true_false is False:
        print('An {} friendly file has now been created! Look for {}_{}_{}_{}_{}.txt'.format(args.output,
              args.group, args.organ, args.dataset, args.orientation, args.output))

    file.close()
