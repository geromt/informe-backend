class ProjectsDTO:
    def __init__(self, from_year, to_year, data, keys, bar_keys):
        self.from_year = from_year
        self.to_year = to_year
        self.data = data
        self.keys = keys
        self.bar_keys = bar_keys

    def to_dict(self):
        return {
            "from": self.from_year,
            "to": self.to_year,
            "data": self.data,
            "keys": self.keys,
            "bar_keys": self.bar_keys
        }
