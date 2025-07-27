from medical_application.appointment import Appointment
from medical_application.contact import Contact
from config.database import get_database

collections = get_database()
doctors_collection = collections["doctors"]
appointment_collection = collections["appointments"]


class Doctor:
    def __init__(self, name: str, password: str, specialisation: str, contact: Contact, ):
        self.name = name
        self.password = password
        self.specialisation: str = specialisation
        self.contact = contact
        self.appointment: 'Appointment' = None
        self._is_logged_in = False
        self.role = "doctor"

    @property
    def is_logged_in(self):
        return self._is_logged_in

    @is_logged_in.setter
    def is_logged_in(self, value):
        self._is_logged_in = value
        doctors_collection.update_one(
            {"contact.email": self.contact.email},
            {"$set": {"_is_logged_in": value}}
        )

    @property
    def role(self):
        return self.role.lower()

    def to_dict(self):
        return {
            "name": self.name,
            "password": self.password,
            "specialisation": self.specialisation,
            "_is_logged_in": self._is_logged_in,
            "role": self.role,
            "contact": {
                "name": self.contact.name,
                "phone_no": self.contact.phone_no,
                "email": self.contact.email,
                "address": {
                    "house_no": self.contact.address.house_no,
                    "street": self.contact.address.street,
                    "city": self.contact.address.city,
                    "state": self.contact.address.state
                }
            }
        }


def get_appointments(self):
    return list(appointment_collection.find({"doctors.email": self.contact.email}))
