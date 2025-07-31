from config.database import get_database
from medical_application.appointment import Appointment
from medical_application.contact import Contact
from medical_application.medical_history import MedicalHistory


class Patient:
    def __init__(self, name, gender, password, contact: Contact, db=None):
        self.name = name
        self.gender = gender
        self.password = password
        self.contact = contact
        self.address = contact.address
        self.patient_id = None
        self.medical_record = MedicalHistory()
        self.appointments: list[Appointment] = []
        self.is_logged_in = False
        self.role = "patient"
        self.db = db or get_database()

    def request_appointment(self, patient_email, doctor_email, reason):
        appointment = Appointment(patient_email, doctor_email, reason)
        self.db["request_appointment"].insert_one(appointment.to_dict())
        return appointment

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def get_medical_record(self):
        return self.medical_record

    def get_appointments(self):
        return self.appointments

    def get_address(self):
        return self.address

    def get_contact(self):
        return self.contact

    def is_logged(self):
        return self.is_logged_in

    def get_password(self):
        return self.password

    def view_doctors(self):
        from medical_application.Admin.clinic_admin import Admin
        admin = Admin("admin")
        return admin.get_all_doctors()

    def to_dict(self):
        return {
            "name": self.name,
            "patient_id": self.patient_id,
            "password": self.password,
            "_is_logged_in": self.is_logged_in,
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
