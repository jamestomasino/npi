class hcp:
    _data = []

    def __init__(self, data):
        self._data = data
        pass

    def get_basic(self):
        try:
            return self._data["results"][0]["basic"]
        except:
            pass

    def get_first_name(self):
        basic = self.get_basic()
        try:
            return basic["first_name"]
        except:
            return ""

    def get_last_name(self):
        basic = self.get_basic()
        try:
            return basic["last_name"]
        except:
            return ""

    def is_active(self):
        basic = self.get_basic()
        try:
            return (basic["status"] == "A")
        except:
            return False

    def last_updated(self):
        basic = self.get_basic()
        try:
            return basic["last_updated"]
        except:
            return False

    def get_addresses(self):
        try:
            addresses = self._data["results"][0]["addresses"]
            valid_addresses = []
            for address in addresses:
                if address["address_purpose"] == "LOCATION":
                    valid_addresses.append(address)
            return valid_addresses
        except:
            pass

