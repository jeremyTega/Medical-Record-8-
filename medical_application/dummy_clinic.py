from datetime import datetime, date

from medical_application.dummy_appointment import Appointment
from medical_application.dummy_doctor import Doctor
from medical_application.medical_history import MedicalHistory
from medical_application.patient import Patient


class Clinic:
    def __init__(self, name):
        self.name = name
        self.patients: dict[str, Patient] = {}
        self.doctors: dict[str, Doctor] = {}
        self.appointments: list[Appointment] = []
        self.apt_counter = 1
        self.medical_histories: list[MedicalHistory] = []
        self.date = date.today()
        self.time = datetime.now().time()

    def register_patient(self, patient: Patient):
        self.patients[patient.generate_patient_id()] = patient

    def register_doctor(self, doctor: Doctor):
        self.doctors[doctor.generate_id()] = doctor

    def search_patient(self, patient_id):
        if patient_id in self.patients:
            return self.patients[patient_id]
        raise ValueError("Patient not found")

    def search_doctor(self, doctor_id):
        if doctor_id in self.doctors:
            return self.doctors[doctor_id]
        raise ValueError("Doctor not found")

    def book_appointment(self, patient_id, doctor_id, apt_date, apt_time,reason):
        apt_id = f"APT: {self.apt_counter}"
        appointment = Appointment(apt_id,apt_date,apt_time,reason)
        self.appointments.append(appointment)
        self.patients[patient_id].add_appointment(appointment)
        self.doctors[doctor_id].add_appointment(appointment)
        self.apt_counter += 1
        return f"Booked: {self.patients[patient_id]} with doctor: {self.doctors[doctor_id]} at time: {apt_time}"

