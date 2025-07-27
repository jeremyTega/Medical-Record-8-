
from datetime import datetime

class Appointment:
    def __init__(self, patient_id: str, doctor_email: str, date_time: datetime, status="CONFIRMED"):
        self.patient_id = patient_id
        self.doctor_email = doctor_email
        self.date_time = date_time
        self.status = status

    def to_dict(self):
        return {
            "patient_id": self.patient_id,
            "doctor_email": self.doctor_email,
            "date_time": self.date_time.isoformat(),
            "status": self.status
        }

