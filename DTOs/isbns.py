class ISBNsDTO:
    def __init__(self, from_year, to_year, time_lapse, data, keys):
        self.from_year = from_year
        self.to_year = to_year
        self.time_lapse = time_lapse
        self.data = data
        self.keys = keys

    def to_dict(self):
        return {
            "from": self.from_year,
            "to": self.to_year,
            "time_lapse": self.time_lapse,
            "data": self.data,
            "keys": self.keys
        }
