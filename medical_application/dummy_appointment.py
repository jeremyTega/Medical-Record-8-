
from datetime import datetime, date, time

from medical_application.diagnosis_entry import validate_str_input

class Appointment:
    def __init__(self,reason:str, apt_date,apt_time):
        validate_str_input(reason)
        self.apt_date = datetime.strptime(apt_date, '%m/%d/%Y').date()
        self.reason = reason
        self.apt_time = datetime.strptime(apt_time, '%H:%M').time()
        self.count = 0
        self.apt_id = None

    def generate_id(self):
        self.apt_id = str(self.count + 1)
        self.count += 1

    @property
    def reason(self):
        return self.reason

    @reason.setter
    def reason(self, reason):
        if type(reason) == str:
            self.reason = reason
        else:
            raise TypeError('reason must be a string')

    @property
    def datetime(self):
        return self.datetime

    @datetime.setter
    def datetime(self, datetime):
        if type(datetime) == datetime:
            self.datetime = datetime

