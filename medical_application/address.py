class Address:
    def __init__(self, house_no:str, street:str, city:str, state:str):
        self._house_no = house_no
        self._street = street
        self._city = city
        self._state = state

    @property
    def house_no(self):
        return self._house_no
    @house_no.setter
    def house_no(self, value):
        self._house_no = value

    @property
    def street(self):
        return self._street
    @street.setter
    def street(self, value):
        self._street = value

    @property
    def city(self):
        return self._city
    @city.setter
    def city(self, value):
        self._city = value

    @property
    def state(self):
        return self._state
    @state.setter
    def state(self, value):
        self._state = value

