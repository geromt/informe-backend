class PatentsDTO:
    def __init__(self, from_year, to_year, data):
        self.from_year = from_year
        self.to_year = to_year
        self.data = data

    def to_dict(self):
        return {
            "from": self.from_year,
            "to": self.to_year,
            "data": self.data,
        }