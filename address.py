class address:
    _data = []

    def __init__(self, data):
        self._data = data
        print (self._data["address_1"])
        print (self._data["address_2"])
        print (self._data["city"])
        print (self._data["state"])
        print (self._data["postal_code"])
        print (self._data["telephone_number"])
