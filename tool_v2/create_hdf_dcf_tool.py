import pandas as pd
import dcf_class
import h5py

def read_excel(sheet, e_col, dcf_col, e_unit_col, dcf_unit_col, skip):
    data = pd.read_excel('dcfs.xlsx', sheet_name=sheet, usecols=(e_col, dcf_col), skiprows=skip)
    units = pd.read_excel('dcfs.xlsx', sheet_name=sheet, usecols=[e_unit_col, dcf_unit_col])
    e_units = units.columns[0]
    dcf_units = units.columns[1]
    
    return dcf_class.DCF(data=data, e_units=e_units, dcf_units=dcf_units)

# Full body data
neutrons_ess_iso = read_excel('ESS_neutrons', 0, 1, 3, 4, 2)
photons_ess_iso = read_excel('ESS_photons', 0, 1, 3, 4, 2)
neutrons_ncrp38_iso = read_excel('NCRP38_neutrons', 0, 1, 3, 4, 2)
protons_icrp116_ap = read_excel('ICRP116_protons', 0, 1, 8, 9, 3)
protons_icrp116_pa = read_excel('ICRP116_protons', 0, 2, 8, 9, 3)
protons_icrp116_llat = read_excel('ICRP116_protons', 0, 3, 8, 9, 3)
protons_icrp116_rlat = read_excel('ICRP116_protons', 0, 4, 8, 9, 3)
protons_icrp116_rot = read_excel('ICRP116_protons', 0, 5, 8, 9, 3)
protons_icrp116_iso = read_excel('ICRP116_protons', 0, 6, 8, 9, 3)
neutrons_icrp116_ap = read_excel('ICRP116_neutrons', 0, 1, 8, 9, 3)
neutrons_icrp116_pa = read_excel('ICRP116_neutrons', 0, 2, 8, 9, 3)
neutrons_icrp116_llat = read_excel('ICRP116_neutrons', 0, 3, 8, 9, 3)
neutrons_icrp116_rlat = read_excel('ICRP116_neutrons', 0, 4, 8, 9, 3)
neutrons_icrp116_rot = read_excel('ICRP116_neutrons', 0, 5, 8, 9, 3)
neutrons_icrp116_iso = read_excel('ICRP116_neutrons', 0, 6, 8, 9, 3)
photons_icrp116_ap = read_excel('ICRP116_photons', 0, 1, 8, 9, 3)
photons_icrp116_pa = read_excel('ICRP116_photons', 0, 2, 8, 9, 3)
photons_icrp116_llat = read_excel('ICRP116_photons', 0, 3, 8, 9, 3)
photons_icrp116_rlat = read_excel('ICRP116_photons', 0, 4, 8, 9, 3)
photons_icrp116_rot = read_excel('ICRP116_photons', 0, 5, 8, 9, 3)
photons_icrp116_iso = read_excel('ICRP116_photons', 0, 6, 8, 9, 3)
electrons_icrp116_ap = read_excel('ICRP116_electrons', 0, 1, 5, 6, 3)
electrons_icrp116_pa = read_excel('ICRP116_electrons', 0, 2, 5, 6, 3)
electrons_icrp116_iso = read_excel('ICRP116_electrons', 0, 3, 5, 6, 3)
positrons_icrp116_ap = read_excel('ICRP116_positrons', 0, 1, 5, 6, 3)
positrons_icrp116_pa = read_excel('ICRP116_positrons', 0, 2, 5, 6, 3)
positrons_icrp116_iso = read_excel('ICRP116_positrons', 0, 3, 5, 6, 3)
neg_muons_icrp116_ap = read_excel('ICRP116_muon-', 0, 1, 5, 6, 3)
neg_muons_icrp116_pa = read_excel('ICRP116_muon-', 0, 2, 5, 6, 3)
neg_muons_icrp116_iso = read_excel('ICRP116_muon-', 0, 3, 5, 6, 3)
pos_muons_icrp116_ap = read_excel('ICRP116_muon+', 0, 1, 5, 6, 3)
pos_muons_icrp116_pa = read_excel('ICRP116_muon+', 0, 2, 5, 6, 3)
pos_muons_icrp116_iso = read_excel('ICRP116_muon+', 0, 3, 5, 6, 3)
neg_pions_icrp116_ap = read_excel('ICRP116_pion-', 0, 1, 5, 6, 3)
neg_pions_icrp116_pa = read_excel('ICRP116_pion-', 0, 2, 5, 6, 3)
neg_pions_icrp116_iso = read_excel('ICRP116_pion-', 0, 3, 5, 6, 3)
pos_pions_icrp116_ap = read_excel('ICRP116_pion+', 0, 1, 5, 6, 3)
pos_pions_icrp116_pa = read_excel('ICRP116_pion+', 0, 2, 5, 6, 3)
pos_pions_icrp116_iso = read_excel('ICRP116_pion+', 0, 3, 5, 6, 3)
helium_icrp116_ap = read_excel('ICRP116_helium', 0, 1, 5, 6, 3)
helium_icrp116_pa = read_excel('ICRP116_helium', 0, 2, 5, 6, 3)
helium_icrp116_iso = read_excel('ICRP116_helium', 0, 3, 5, 6, 3)

# Eye data
eye_photons_icrp116_ap = read_excel('ICRP116_photons_eye', 0, 1, 7, 8, 3)
eye_photons_icrp116_pa = read_excel('ICRP116_photons_eye', 0, 2, 7, 8, 3)
eye_photons_icrp116_lat = read_excel('ICRP116_photons_eye', 0, 3, 7, 8, 3)
eye_photons_icrp116_rot = read_excel('ICRP116_photons_eye', 0, 4, 7, 8, 3)
eye_photons_icrp116_iso = read_excel('ICRP116_photons_eye', 0, 5, 7, 8, 3)
eye_electrons_icrp116_ap = read_excel('ICRP116_electrons_eye', 0, 1, 5, 6, 3)
eye_electrons_icrp116_pa = read_excel('ICRP116_electrons_eye', 0, 2, 5, 6, 3)
eye_electrons_icrp116_iso = read_excel('ICRP116_electrons_eye', 0, 3, 5, 6, 3)
eye_neutrons_icrp116_ap = read_excel('ICRP116_neutrons_eye', 0, 1, 7, 8, 3)
eye_neutrons_icrp116_pa = read_excel('ICRP116_neutrons_eye', 0, 2, 7, 8, 3)
eye_neutrons_icrp116_lat = read_excel('ICRP116_neutrons_eye', 0, 3, 7, 8, 3)
eye_neutrons_icrp116_rot = read_excel('ICRP116_neutrons_eye', 0, 4, 7, 8, 3)
eye_neutrons_icrp116_iso = read_excel('ICRP116_neutrons_eye', 0, 5, 7, 8, 3)

dcffile = h5py.File('DCFfile.h5', 'w')

ess = dcffile.create_group('ESS')
ess_full_body = ess.create_group('full_body')
ess_full_body.attrs['energy_units'] = neutrons_ess_iso.e_units
ess_full_body.attrs['dcf_units'] = neutrons_ess_iso.dcf_units

ncrp38 = dcffile.create_group('NCRP38')
ncrp38_full_body = ncrp38.create_group('full_body')
ncrp38_full_body.attrs['energy_units'] = neutrons_ncrp38_iso.e_units
ncrp38_full_body.attrs['dcf_units'] = neutrons_ncrp38_iso.dcf_units

icrp116 = dcffile.create_group('ICRP116')
icrp116_full_body = icrp116.create_group('full_body')
icrp116_full_body.attrs['energy_units'] = neutrons_icrp116_iso.e_units
icrp116_full_body.attrs['dcf_units'] = neutrons_icrp116_iso.dcf_units
icrp116_eyes = icrp116.create_group('eyes')
icrp116_eyes.attrs['energy_units'] = eye_neutrons_icrp116_iso.e_units
icrp116_eyes.attrs['dcf_units'] = eye_neutrons_icrp116_iso.dcf_units

ess_neutrons_group = ess_full_body.create_group('neutrons')
ess_neutrons_group.create_dataset('ISO', data=neutrons_ess_iso.data)

ess_photons_group = ess_full_body.create_group('photons')
ess_photons_group.create_dataset('ISO', data=photons_ess_iso.data)

ncrp38_neutrons_group = ncrp38_full_body.create_group('neutrons')
ncrp38_neutrons_group.create_dataset('ISO', data=neutrons_ncrp38_iso.data)

icrp116_protons_group = icrp116_full_body.create_group('protons')
icrp116_protons_group.create_dataset('AP', data=protons_icrp116_ap.data)
icrp116_protons_group.create_dataset('PA', data=protons_icrp116_pa.data)
icrp116_protons_group.create_dataset('LLAT', data=protons_icrp116_llat.data)
icrp116_protons_group.create_dataset('RLAT', data=protons_icrp116_rlat.data)
icrp116_protons_group.create_dataset('ROT', data=protons_icrp116_rot.data)
icrp116_protons_group.create_dataset('ISO', data=protons_icrp116_iso.data)

icrp116_neutrons_group = icrp116_full_body.create_group('neutrons')
icrp116_neutrons_group.create_dataset('AP', data=neutrons_icrp116_ap.data)
icrp116_neutrons_group.create_dataset('PA', data=neutrons_icrp116_pa.data)
icrp116_neutrons_group.create_dataset('LLAT', data=neutrons_icrp116_llat.data)
icrp116_neutrons_group.create_dataset('RLAT', data=neutrons_icrp116_rlat.data)
icrp116_neutrons_group.create_dataset('ROT', data=neutrons_icrp116_rot.data)
icrp116_neutrons_group.create_dataset('ISO', data=neutrons_icrp116_iso.data)

icrp116_photons_group = icrp116_full_body.create_group('photons')
icrp116_photons_group.create_dataset('AP', data=photons_icrp116_ap.data)
icrp116_photons_group.create_dataset('PA', data=photons_icrp116_pa.data)
icrp116_photons_group.create_dataset('LLAT', data=photons_icrp116_llat.data)
icrp116_photons_group.create_dataset('RLAT', data=photons_icrp116_rlat.data)
icrp116_photons_group.create_dataset('ROT', data=photons_icrp116_rot.data)
icrp116_photons_group.create_dataset('ISO', data=photons_icrp116_iso.data)

icrp116_electrons_group = icrp116_full_body.create_group('electrons')
icrp116_electrons_group.create_dataset('AP', data=electrons_icrp116_ap.data)
icrp116_electrons_group.create_dataset('PA', data=electrons_icrp116_pa.data)
icrp116_electrons_group.create_dataset('ISO', data=electrons_icrp116_iso.data)

icrp116_positrons_group = icrp116_full_body.create_group('positrons')
icrp116_positrons_group.create_dataset('AP', data=positrons_icrp116_ap.data)
icrp116_positrons_group.create_dataset('PA', data=positrons_icrp116_pa.data)
icrp116_positrons_group.create_dataset('ISO', data=positrons_icrp116_iso.data)

icrp116_neg_muons_group = icrp116_full_body.create_group('muon-')
icrp116_neg_muons_group.create_dataset('AP', data=neg_muons_icrp116_ap.data)
icrp116_neg_muons_group.create_dataset('PA', data=neg_muons_icrp116_pa.data)
icrp116_neg_muons_group.create_dataset('ISO', data=neg_muons_icrp116_iso.data)

icrp116_pos_muon_group = icrp116_full_body.create_group('muon+')
icrp116_pos_muon_group.create_dataset('AP', data=pos_muons_icrp116_ap.data)
icrp116_pos_muon_group.create_dataset('PA', data=pos_muons_icrp116_pa.data)
icrp116_pos_muon_group.create_dataset('ISO', data=pos_muons_icrp116_iso.data)

icrp116_neg_pions_group = icrp116_full_body.create_group('pion-')
icrp116_neg_pions_group.create_dataset('AP', data=neg_pions_icrp116_ap.data)
icrp116_neg_pions_group.create_dataset('PA', data=neg_pions_icrp116_pa.data)
icrp116_neg_pions_group.create_dataset('ISO', data=neg_pions_icrp116_iso.data)

icrp116_pos_pions_group = icrp116_full_body.create_group('pion+')
icrp116_pos_pions_group.create_dataset('AP', data=pos_pions_icrp116_ap.data)
icrp116_pos_pions_group.create_dataset('PA', data=pos_pions_icrp116_pa.data)
icrp116_pos_pions_group.create_dataset('ISO', data=pos_pions_icrp116_iso.data)

icrp116_helium_group = icrp116_full_body.create_group('helium')
icrp116_helium_group.create_dataset('AP', data=helium_icrp116_ap.data)
icrp116_helium_group.create_dataset('PA', data=helium_icrp116_pa.data)
icrp116_helium_group.create_dataset('ISO', data=helium_icrp116_iso.data)

icrp116_eyes_photons_group = icrp116_eyes.create_group('photons')
icrp116_eyes_photons_group.create_dataset('AP', data=eye_photons_icrp116_ap.data)
icrp116_eyes_photons_group.create_dataset('PA', data=eye_photons_icrp116_pa.data)
icrp116_eyes_photons_group.create_dataset('LAT', data=eye_photons_icrp116_lat.data)
icrp116_eyes_photons_group.create_dataset('ROT', data=eye_photons_icrp116_rot.data)
icrp116_eyes_photons_group.create_dataset('ISO', data=eye_photons_icrp116_iso.data)

icrp116_eyes_electrons_group = icrp116_eyes.create_group('electrons')
icrp116_eyes_electrons_group.create_dataset('AP', data=eye_electrons_icrp116_ap.data)
icrp116_eyes_electrons_group.create_dataset('PA', data=eye_electrons_icrp116_pa.data)
icrp116_eyes_electrons_group.create_dataset('ISO', data=eye_electrons_icrp116_iso.data)

icrp116_eyes_neutrons_group = icrp116_eyes.create_group('neutrons')
icrp116_eyes_neutrons_group.create_dataset('AP', data=eye_neutrons_icrp116_ap.data)
icrp116_eyes_neutrons_group.create_dataset('PA', data=eye_neutrons_icrp116_pa.data)
icrp116_eyes_neutrons_group.create_dataset('LAT', data=eye_neutrons_icrp116_lat.data)
icrp116_eyes_neutrons_group.create_dataset('ROT', data=eye_neutrons_icrp116_rot.data)
icrp116_eyes_neutrons_group.create_dataset('ISO', data=eye_neutrons_icrp116_iso.data)

dcffile.close()
