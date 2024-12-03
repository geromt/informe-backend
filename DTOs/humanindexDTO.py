class HumanindexDTO:
    def __init__(self, from_year, to_year, time_lapse, data, keys):
        self.from_year = from_year
        self.to_year = to_year
        self.time_lapse = time_lapse
        self.keys = keys
        self.data = data

    def to_dict(self):
        return {
            "from": self.from_year,
            "to": self.to_year,
            "time_lapse": self.time_lapse,
            "data": self.data,
            "keys": self.keys
        }