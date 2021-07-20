import pandas as pd
import dcf_class
import h5py

neutrons_ess_iso = dcf_class.DCF('ESS_neutrons', 0, 1, 3, 4, 2, 'neutrons', 'ISO')
photons_ess_iso = dcf_class.DCF('ESS_photons', 0, 1, 3, 4, 2, 'photons', 'ISO')
neutrons_ncrp38_iso = dcf_class.DCF('NCRP38_neutrons', 0, 1, 3, 4, 2, 'neutrons', 'ISO')
protons_icrp116_ap = dcf_class.DCF('ICRP116_protons', 0, 1, 8, 9, 3, 'protons', 'AP')
protons_icrp116_pa = dcf_class.DCF('ICRP116_protons', 0, 2, 8, 9, 3, 'protons', 'PA')
protons_icrp116_llat = dcf_class.DCF('ICRP116_protons', 0, 3, 8, 9, 3, 'protons', 'LLAT')
protons_icrp116_rlat = dcf_class.DCF('ICRP116_protons', 0, 4, 8, 9, 3, 'protons', 'RLAT')
protons_icrp116_rot = dcf_class.DCF('ICRP116_protons', 0, 5, 8, 9, 3, 'protons', 'ROT')
protons_icrp116_iso = dcf_class.DCF('ICRP116_protons', 0, 6, 8, 9, 3, 'protons', 'ISO')
neutrons_icrp116_ap = dcf_class.DCF('ICRP116_neutrons', 0, 1, 8, 9, 3, 'neutrons', 'AP')
neutrons_icrp116_pa = dcf_class.DCF('ICRP116_neutrons', 0, 2, 8, 9, 3, 'neutrons', 'PA')
neutrons_icrp116_llat = dcf_class.DCF('ICRP116_neutrons', 0, 3, 8, 9, 3, 'neutrons', 'LLAT')
neutrons_icrp116_rlat = dcf_class.DCF('ICRP116_neutrons', 0, 4, 8, 9, 3, 'neutrons', 'RLAT')
neutrons_icrp116_rot = dcf_class.DCF('ICRP116_neutrons', 0, 5, 8, 9, 3, 'neutrons', 'ROT')
neutrons_icrp116_iso = dcf_class.DCF('ICRP116_neutrons', 0, 6, 8, 9, 3, 'neutrons', 'ISO')
photons_icrp116_ap = dcf_class.DCF('ICRP116_photons', 0, 1, 8, 9, 3, 'photons', 'AP')
photons_icrp116_pa = dcf_class.DCF('ICRP116_photons', 0, 2, 8, 9, 3, 'photons', 'PA')
photons_icrp116_llat = dcf_class.DCF('ICRP116_photons', 0, 3, 8, 9, 3, 'photons', 'LLAT')
photons_icrp116_rlat = dcf_class.DCF('ICRP116_photons', 0, 4, 8, 9, 3, 'photons', 'RLAT')
photons_icrp116_rot = dcf_class.DCF('ICRP116_photons', 0, 5, 8, 9, 3, 'photons', 'ROT')
photons_icrp116_iso = dcf_class.DCF('ICRP116_photons', 0, 6, 8, 9, 3, 'photons', 'ISO')
electrons_icrp116_ap = dcf_class.DCF('ICRP116_electrons', 0, 1, 5, 6, 3, 'electrons', 'AP')
electrons_icrp116_pa = dcf_class.DCF('ICRP116_electrons', 0, 2, 5, 6, 3, 'electrons', 'PA')
electrons_icrp116_iso = dcf_class.DCF('ICRP116_electrons', 0, 3, 5, 6, 3, 'electrons', 'ISO')
positrons_icrp116_ap = dcf_class.DCF('ICRP116_positrons', 0, 1, 5, 6, 3, 'positrons', 'AP')
positrons_icrp116_pa = dcf_class.DCF('ICRP116_positrons', 0, 2, 5, 6, 3, 'positrons', 'PA')
positrons_icrp116_iso = dcf_class.DCF('ICRP116_positrons', 0, 3, 5, 6, 3, 'positrons', 'ISO')
neg_muons_icrp116_ap = dcf_class.DCF('ICRP116_muon-', 0, 1, 5, 6, 3, 'muon-', 'AP')
neg_muons_icrp116_pa = dcf_class.DCF('ICRP116_muon-', 0, 2, 5, 6, 3, 'muon-', 'PA')
neg_muons_icrp116_iso = dcf_class.DCF('ICRP116_muon-', 0, 3, 5, 6, 3, 'muon-', 'ISO')
pos_muons_icrp116_ap = dcf_class.DCF('ICRP116_muon+', 0, 1, 5, 6, 3, 'muon+', 'AP')
pos_muons_icrp116_pa = dcf_class.DCF('ICRP116_muon+', 0, 2, 5, 6, 3, 'muon+', 'PA')
pos_muons_icrp116_iso = dcf_class.DCF('ICRP116_muon+', 0, 3, 5, 6, 3, 'muon+', 'ISO')
neg_pions_icrp116_ap = dcf_class.DCF('ICRP116_pion-', 0, 1, 5, 6, 3, 'pion-', 'AP')
neg_pions_icrp116_pa = dcf_class.DCF('ICRP116_pion-', 0, 2, 5, 6, 3, 'pion-', 'PA')
neg_pions_icrp116_iso = dcf_class.DCF('ICRP116_pion-', 0, 3, 5, 6, 3, 'pion-', 'ISO')
pos_pions_icrp116_ap = dcf_class.DCF('ICRP116_pion+', 0, 1, 5, 6, 3, 'pion+', 'AP')
pos_pions_icrp116_pa = dcf_class.DCF('ICRP116_pion+', 0, 2, 5, 6, 3, 'pion+', 'PA')
pos_pions_icrp116_iso = dcf_class.DCF('ICRP116_pion+', 0, 3, 5, 6, 3, 'pion+', 'ISO')
helium_icrp116_ap = dcf_class.DCF('ICRP116_helium', 0, 1, 5, 6, 3, 'helium', 'AP')
helium_icrp116_pa = dcf_class.DCF('ICRP116_helium', 0, 2, 5, 6, 3, 'helium', 'PA')
helium_icrp116_iso = dcf_class.DCF('ICRP116_helium', 0, 3, 5, 6, 3, 'helium', 'ISO')


dcffile = h5py.File('DCFfile.h5', 'w')
ess = dcffile.create_group('ESS')
ess.attrs['energy_units'] = neutrons_ess_iso.e_units
ess.attrs['dcf_units'] = neutrons_ess_iso.dcf_units
ncrp38 = dcffile.create_group('NCRP38')
ncrp38.attrs['energy_units'] = neutrons_ncrp38_iso.e_units
ncrp38.attrs['dcf_units'] = neutrons_ncrp38_iso.dcf_units
icrp116 = dcffile.create_group('ICRP116')
icrp116.attrs['energy_units'] = neutrons_icrp116_iso.e_units
icrp116.attrs['dcf_units'] = neutrons_icrp116_iso.dcf_units

ess_neutrons_group = ess.create_group('neutrons')
ess_neutrons_group.create_dataset('ISO', data=neutrons_ess_iso.data)

ess_photons_group = ess.create_group('photons')
ess_photons_group.create_dataset('photons', data=photons_ess_iso.data)

ncrp38_neutrons_group = ncrp38.create_group('neutrons')
ncrp38_neutrons_group.create_dataset('neutrons', data=neutrons_ncrp38_iso.data)

icrp116_protons_group = icrp116.create_group('protons')
icrp116_protons_group.create_dataset('AP', data=protons_icrp116_ap.data)
icrp116_protons_group.create_dataset('PA', data=protons_icrp116_pa.data)
icrp116_protons_group.create_dataset('LLAT', data=protons_icrp116_llat.data)
icrp116_protons_group.create_dataset('RLAT', data=protons_icrp116_rlat.data)
icrp116_protons_group.create_dataset('ROT', data=protons_icrp116_rot.data)
icrp116_protons_group.create_dataset('ISO', data=protons_icrp116_iso.data)

icrp116_neutrons_group = icrp116.create_group('neutrons')
icrp116_neutrons_group.create_dataset('AP', data=neutrons_icrp116_ap.data)
icrp116_neutrons_group.create_dataset('PA', data=neutrons_icrp116_pa.data)
icrp116_neutrons_group.create_dataset('LLAT', data=neutrons_icrp116_llat.data)
icrp116_neutrons_group.create_dataset('RLAT', data=neutrons_icrp116_rlat.data)
icrp116_neutrons_group.create_dataset('ROT', data=neutrons_icrp116_rot.data)
icrp116_neutrons_group.create_dataset('ISO', data=neutrons_icrp116_iso.data)

icrp116_photons_group = icrp116.create_group('photons')
icrp116_photons_group.create_dataset('AP', data=photons_icrp116_ap.data)
icrp116_photons_group.create_dataset('PA', data=photons_icrp116_pa.data)
icrp116_photons_group.create_dataset('LLAT', data=photons_icrp116_llat.data)
icrp116_photons_group.create_dataset('RLAT', data=photons_icrp116_rlat.data)
icrp116_photons_group.create_dataset('ROT', data=photons_icrp116_rot.data)
icrp116_photons_group.create_dataset('ISO', data=photons_icrp116_iso.data)

icrp116_electrons_group = icrp116.create_group('electrons')
icrp116_electrons_group.create_dataset('AP', data=electrons_icrp116_ap.data)
icrp116_electrons_group.create_dataset('PA', data=electrons_icrp116_pa.data)
icrp116_electrons_group.create_dataset('ISO', data=electrons_icrp116_iso.data)

icrp116_positrons_group = icrp116.create_group('positrons')
icrp116_positrons_group.create_dataset('AP', data=positrons_icrp116_ap.data)
icrp116_positrons_group.create_dataset('PA', data=positrons_icrp116_pa.data)
icrp116_positrons_group.create_dataset('ISO', data=positrons_icrp116_iso.data)

icrp116_neg_muons_group = icrp116.create_group('muon-')
icrp116_neg_muons_group.create_dataset('AP', data=neg_muons_icrp116_ap.data)
icrp116_neg_muons_group.create_dataset('PA', data=neg_muons_icrp116_pa.data)
icrp116_neg_muons_group.create_dataset('ISO', data=neg_muons_icrp116_iso.data)

icrp116_pos_muon_group = icrp116.create_group('muon+')
icrp116_pos_muon_group.create_dataset('AP', data=pos_muons_icrp116_ap.data)
icrp116_pos_muon_group.create_dataset('PA', data=pos_muons_icrp116_pa.data)
icrp116_pos_muon_group.create_dataset('ISO', data=pos_muons_icrp116_iso.data)

icrp116_neg_pions_group = icrp116.create_group('pion-')
icrp116_neg_pions_group.create_dataset('AP', data=neg_pions_icrp116_ap.data)
icrp116_neg_pions_group.create_dataset('PA', data=neg_pions_icrp116_pa.data)
icrp116_neg_pions_group.create_dataset('ISO', data=neg_pions_icrp116_iso.data)

icrp116_pos_pions_group = icrp116.create_group('pion+')
icrp116_pos_pions_group.create_dataset('AP', data=pos_pions_icrp116_ap.data)
icrp116_pos_pions_group.create_dataset('PA', data=pos_pions_icrp116_pa.data)
icrp116_pos_pions_group.create_dataset('ISO', data=pos_pions_icrp116_iso.data)

icrp116_helium_group = icrp116.create_group('helium')
icrp116_helium_group.create_dataset('AP', data=helium_icrp116_ap.data)
icrp116_helium_group.create_dataset('PA', data=helium_icrp116_pa.data)
icrp116_helium_group.create_dataset('ISO', data=helium_icrp116_iso.data)

dcffile.close()

'''dcffile = h5py.File('DCFfile.h5', 'r')

print(dcffile.get('/ICRP116').attrs['dcf_units'])

dcffile.close()'''
