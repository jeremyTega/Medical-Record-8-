from medical_application import contact
from medical_application.dummy_appointment import Appointment
from medical_application.contact import Contact
from medical_application.diagnosis_entry import DiagnosisEntry


class Doctor:
    def __init__(self,name):
        self.doctor_id = None
        self.count = 10
        self.name = name
        self.specialization = None
        self.contact = contact
        self.diagnosis = DiagnosisEntry
        self.appointments: list[Appointment] = []

    def add_appointment(self,appointment):
        self.appointments.append(appointment)

    def get_appointments(self):
        return self.appointments
    def generate_id(self):
        self.doctor_id = "D" + str(self.count + 1)
        self.count += 1
        return self.doctor_id
