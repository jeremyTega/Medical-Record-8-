
from datetime import datetime, date, time


class Appointment:
    def __init__(self, appointmentId:int, reason:str, datetime:datetime):
        self.appointmentId = appointmentId
        self.reason = reason
        self.datetime = datetime.today()

    @property
    def appointmentId(self):
        return self.appointmentId

    @appointmentId.setter
    def appointmentId(self, appointmentId):
        if  type(appointmentId) == int:
            self.appointmentId = appointmentId
        else:
            raise TypeError('appointmentId must be an integer')

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

