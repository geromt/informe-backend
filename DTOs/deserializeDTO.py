class DeserializeDTO:
    def __init__(self, data_type, data_key, data):
        self.data_type = data_type
        self.data_key = data_key
        self.data = data
        self.rows = len(data)

    def to_dict(self):
        return {
            "type": self.data_type,
            "datakey": self.data_key,
            "data": self.data,
            "length": self.rows
        }