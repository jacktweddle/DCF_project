import pandas as pd
import numpy as np
import h5py
import unit_conversions as uc
import matplotlib.pyplot as plt


def convert(func, x):
    for i in range(0, len(x)):
        x[i] = func(x[i])


def rem_to_microsv(x):
    return uc.micro(uc.rem_to_sv(x))


def psv_cm2_to_microsv_hour(x):
    return uc.mega(3600 * x)


def create_file(group, dataset, orientation, data):
    np.savetxt('energies_prelim.txt', data['E (MeV)'], fmt='%.2e')
    if group == 'ICRP116':
        np.savetxt('dcfs_prelim.txt', data[orientation], fmt='%.2e')
    else:
        np.savetxt('dcfs_prelim.txt', data['DCF (microSv/h per n/cm2/s)'], fmt='%.2e')
    with open('energies_prelim.txt', 'r') as f_e:
        lines = f_e.read().split('\n')
        new_energy = []
        new_energy_line = '   '
        for x in lines:
            if len(new_energy_line) < 80 and len(new_energy_line + ' ' + x) < 80:
                new_energy_line += ' ' + x
            if len(new_energy_line) >= 80 or len(new_energy_line + ' ' + x) > 80:
                new_energy.append(new_energy_line)
                new_energy_line = '   '
    with open('dcfs_prelim.txt', 'r') as f_dcf:
        lines = f_dcf.read().split('\n')
        new_dcf = []
        new_dcf_line = '   '
        for x in lines:
            if len(new_dcf_line) < 80 and len(new_dcf_line + ' ' + x) < 80:
                new_dcf_line += ' ' + x
            if len(new_dcf_line) >= 80 or len(new_dcf_line + ' ' + x) > 80:
                new_dcf.append(new_dcf_line)
                new_dcf_line = '   '
    with open('{}_{}_{}_mcnp.txt'.format(group, dataset, orientation), 'w') as new_f:
        new_f.write('DEXX $ Energy (MeV)\n')
        new_f.write('\n'.join(new_energy))
        new_f.write('\n')
        new_f.write('DFXX $ DCF (microSv/h per n/cm2/s)\n')
        new_f.write('\n'.join(new_dcf))


dcffile = h5py.File('DCFfile.h5', 'r')
print(dcffile.keys(), '\n')
input_group = str(input('Which data group would you like? Please enter without the /.\n'))
group = dcffile.get('/' + input_group)
print(group.keys(), '\n')
input_dataset = str(input('Which dataset would you like? Please enter without the /.\n'))
path = '/' + input_group + '/' + input_dataset

if input_group == 'ESS':
    data = pd.DataFrame(dcffile.get(path), columns=['E (MeV)', 'DCF (microSv/h per n/cm2/s)']).reset_index(drop=True)
    orientation = 'ISO'
    data.plot(kind='line', x='E (MeV)', y='DCF (microSv/h per n/cm2/s)', ylabel='DCF (microSv/h per n/cm2/s)', legend=False)
if input_group == 'NCRP38':
    data = pd.DataFrame(dcffile.get(path), columns=['E (MeV)', 'DCF (microSv/h per n/cm2/s)']).reset_index(drop=True)
    orientation = 'ISO'
    dose = np.array(data['DCF (microSv/h per n/cm2/s)'])
    convert(rem_to_microsv, dose)
    data['DCF (microSv/h per n/cm2/s)'] = dose
    data.plot(kind='line', x='E (MeV)', y='DCF (microSv/h per n/cm2/s)', ylabel='DCF (microSv/h per n/cm2/s)', legend=False)
if input_group == 'ICRP116':
    if input_dataset in ['protons', 'photons', 'neutrons']:
        orientation = str(input('Which orientation would you like? Select from AP, PA, LLAT, RLAT, ROT, ISO.\n'))
        all_data = pd.DataFrame(dcffile.get(path), columns=['E (MeV)', 'AP', 'PA', 'LLAT', 'RLAT', 'ROT', 'ISO']).reset_index(drop=True)
    else:
        orientation = str(input('Which orientation would you like? Select from AP, PA, ISO.\n'))
        all_data = pd.DataFrame(dcffile.get(path), columns=['E (MeV)', 'AP', 'PA', 'ISO']).reset_index(drop=True)
    data = all_data.loc[:, ('E (MeV)', orientation)]
    dose = np.array(data.loc[:, orientation])
    convert(psv_cm2_to_microsv_hour, dose)
    data.loc[:, orientation] = dose
    data.plot(kind='line', x='E (MeV)', y=orientation, ylabel='DCF (microSv/h per n/cm2/s)', legend=False)

dcffile.close()

create_file(input_group, input_dataset, orientation, data)
print('Your data has been plotted and a file has now been created! Look for group_dataset_mcnp.txt')
