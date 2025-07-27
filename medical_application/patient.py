from datetime import datetime,date

from config.database import get_database
from medical_application.address import Address
from medical_application.dummy_appointment import Appointment
from medical_application.contact import Contact
from medical_application.medical_history import MedicalHistory
collections = get_database()


def validate_str_input(string:str):
    if string is None:
        raise ValueError(f'{string} cannot be None')
    if type(string) is not str:
        raise ValueError(f'{string} must be a string')
    if string.strip() == "":
        raise ValueError(f'{string} cannot be empty')
def validate_gender(gender:str):
    validate_str_input(gender)
    if gender != "male" and gender != "female":
        raise ValueError(f'{gender} must be "male" or "female"')


def set_date_of_birth(dob):
    try:
        dob_date = datetime.strptime(dob, "%d/%m/%Y").date()
    except ValueError:
        raise ValueError(f"{dob} is not in the correct format DD/MM/YYYY")

    if dob_date > date.today():
        raise ValueError(f"{dob} cannot be in the future")


class Patient:
    def __init__(self,name,gender,dob):
        validate_str_input(name)
        validate_gender(gender)
        self.name=name
        self.gender=gender
        self.password = None
        self.contact = None
        self.address = None
        set_date_of_birth(dob)
        self.dob = dob
        self.counter = 100
        self.patient_id = None
        self.medical_record = MedicalHistory()
        self.appointments: list[Appointment] = []
        self.is_logged_in = False

    def generate_patient_id(self):
        self.patient_id = "P" + str(self.counter + 1)
        self.counter += 1
        return self.patient_id

    def get_medical_record(self):
        return self.medical_record

    def get_appointments(self):
        return self.appointments

    def get_date_of_birth(self):
        return self.dob

    def set_address(self, house_no, street, city, state):
        if house_no < 0:
            raise ValueError(f'{house_no} must be greater than 0')
        house_no = house_no
        validate_str_input(street)
        validate_str_input(city)
        validate_str_input(state)
        self.address = Address(house_no, street, city, state)

    def get_address(self):
        return self.address

    def create_contact(self,phone,email,address:Address):
        validate_str_input(phone)
        validate_str_input(email)
        self.contact = Contact(self.name, phone, email, address)

    def get_contact(self):
        return self.contact

    def is_logged(self):
        return self.is_logged_in

    def set_password(self,password):
        validate_str_input(password)
        if len(password) < 8:
            raise ValueError(f'{password} must be at least 8 characters long')
        self.password = password

    def get_password(self):
        return self.password

    def log_in(self,email,password):
        if email != self.get_contact().email:
            raise ValueError(f'{email} does not match your email')
        if password != self.get_password():
            raise ValueError("Incorrect password")
        self.is_logged_in = True


    def request_appointment(self,patient_email, doctor_email, reason):
        #validate_str_input(reason)
        appointment = Appointment(patient_email,doctor_email,reason)
        collections["request Appointment"].insert_one(appointment.to_dict())
        return appointment

    def add_appointment(self,appointment):
        self.appointments.append(appointment)


    def to_dict(self):
     return {
        "name": self.name,
         "patient_id": getattr(self, "P"),
         "Date of Birth": self.get_date_of_birth(),
        "password": self.get_password(),
        "_is_logged_in": self.is_logged(),
        "contact": {
            "name": self.get_contact().name,
            "gender": self.gender,
            "phone_no": self.get_contact().phone_no,
            "email": self.get_contact().email,
            "address": {
                "house_no": self.get_contact().address.house_no,
                "street": self.get_address().street,
                "city": self.get_address().city,
                "state": self.get_address().state
            }
        }
    }




    