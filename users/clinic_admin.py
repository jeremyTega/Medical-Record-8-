from config.database import doctors_collection
from medical_application.doctor import Doctor
from validators.auth_validator import validate_non_empty, validate_email_format


class Admin:
    def __init__(self, username):
        self.username = username

    def create_doctor(self,name,password,specialisation,my_Contact):
        validate_non_empty("Name", name)
        validate_non_empty("Password", password)
        validate_non_empty("Specialisation", specialisation)
        validate_non_empty("Contact", my_Contact)
        validate_email_format(my_Contact.email)
        doctor = Doctor(name,password,specialisation,my_Contact)
        result = doctors_collection.insert_one(doctor.to_dict())
        return doctor

