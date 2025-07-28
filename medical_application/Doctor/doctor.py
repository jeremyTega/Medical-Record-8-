from medical_application.appointment import Appointment
from medical_application.contact import Contact
from config.database import get_database
#from users.clinic_admin import Admin

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
        return self._role.lower()
    @role.setter
    def role(self, value):
        self._role = value

    def to_dict(self):
        return {
            "name": self.name,
            "password": self.password,
            "specialisation": self.specialisation,
            "_is_logged_in": self._is_logged_in,
            "role": self.role,
            "contact": {
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

    def approve_appointment_by_id(self, appointment_id: str, appointment_date: str):
        from medical_application.Admin.clinic_admin import Admin
        return Admin.approve_appointment(self, appointment_id, appointment_date)

    def add_diagnosis(self,patient_email: str, diagnosis_type: str, medication: str):
        from medical_application.Admin.clinic_admin import Admin
        return Admin.add_diagnosis(self, patient_email, diagnosis_type, medication)


