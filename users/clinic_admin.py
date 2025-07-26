from config.database import get_database
collections = get_database()
doctors_collection = collections["doctors"]
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

    # def create_patient(self, name,age,gender):
    #     validate_non_empty("Name", name)
    #     validate_non_empty("Age", age)
    #     validate_non_empty("Gender", gender)
    #     patient = Patient(name,age,gender)
    #     result = patients_collection.insert_one(patient.to_dict())

    # def get_one_patient(self,name):
    #     validate_non_empty("Name", name)
    #     result = patients_collection.find_one({"Name": name})
    #     return result
