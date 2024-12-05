class DeserializeDocumentsDTO:
    def __init__(self, datakey, data):
        self.datakey = datakey
        self.data = data
        self.rows = len(data)

    def to_dict(self):
        return {
            "type": self.datakey,
            "data": self.data,
            "length": self.rows
        }