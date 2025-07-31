import random
from datetime import datetime

class Appointment:
    def __init__(self, patient_id: str, doctor_id: str, reason:str):
        appointment_id = self.generate_id()
        self.patient_id = patient_id
        self.doctor_email = doctor_id
        self.date_time = datetime.now()
        self.reason = reason
        self.status = "pending"

    def generate_id(self):
        return str(random.randint(1000, 9999))

    def to_dict(self):
        return {
            "appointment_id": self.patient_id,
            "patient_id": self.patient_id,
            "doctor_email": self.doctor_email,
            "date_time": self.date_time,
            "reason": self.reason,
            "status": self.status
        }

