import pandas as pd

class DCF:
    def __init__(self, sheet, e_col, dcf_col, e_unit_col, dcf_unit_col, skip, particle, orientation):
        self.sheet = sheet
        self.e_col = e_col
        self.dcf_col = dcf_col
        self.e_unit_col = e_unit_col
        self.dcf_unit_col = dcf_unit_col
        self.skip = skip
        self.particle = particle
        self.orientation = orientation
        self.data = pd.read_excel('dcfs.xlsx', sheet_name=self.sheet, usecols=(self.e_col, self.dcf_col), skiprows=self.skip)
        self.units = pd.read_excel('dcfs.xlsx', sheet_name=self.sheet, usecols=[self.e_unit_col, self.dcf_unit_col])
        self.e_units = self.units.columns[0]
        self.dcf_units = self.units.columns[1]