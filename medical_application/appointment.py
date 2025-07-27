
from datetime import datetime

class Appointment:
    def __init__(self, patient_id: str, doctor_id: str, reason:str,status:"pending"):
        self.patient_id = patient_id
        self.doctor_email = doctor_id
        self.date_time = datetime.now(),
        self.reason = reason
        self.status = status

    def to_dict(self):
        return {
            "patient_id": self.patient_id,
            "doctor_email": self.doctor_email,
            "date_time": self.date_time.isoformat(),
            "reason": self.reason,
            #"status": self.status
        }

