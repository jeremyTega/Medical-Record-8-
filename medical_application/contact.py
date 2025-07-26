from medical_application.address import Address

class Contact:
    def __init__(self, name: str, phone_no: str, email: str, address: Address):
        self._name = name
        self._phone_no = phone_no
        self._email = email
        self._address = address

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def phone_no(self):
        return self._phone_no

    @phone_no.setter
    def phone_no(self, value):
        self._phone_no = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value: Address):
        if not isinstance(value, Address):
            raise ValueError("address must be an instance of Address")
        self._address = value

    def to_dict(self):
        return {
            "name": self.name,
            "phone_no": self.phone_no,
            "email": self.email,
            "address": self.address.to_dict()
        }

    @staticmethod
    def from_dict(data: dict):
        return Contact(
            name=data.get("name", ""),
            phone_no=data.get("phone_no", ""),
            email=data.get("email", ""),
            address=Address.from_dict(data.get("address", {}))
        )