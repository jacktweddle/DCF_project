class DCF:
    def __init__(self, data, e_units, dcf_units, group=None, organ=None, particle=None, orientation=None, path=None):
        self.data = data
        self.e_units = e_units
        self.dcf_units = dcf_units
        self.group = group
        self.particle = particle
        self.orientation = orientation
        self.organ = organ
        self.path = path
