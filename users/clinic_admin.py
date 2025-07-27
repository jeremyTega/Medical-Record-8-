from config.database import get_database
from medical_application.appointment import Appointment

collections = get_database()
doctors_collection = collections["doctors"]
patients_collection = collections["patients"]

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

    def login_user(self, email: str, password: str):

        doctor_data = doctors_collection.find_one({"contact.email": email, "password": password})
        if doctor_data:
            doctors_collection.update_one(
                {"contact.email": email},
                {"$set": {"_is_logged_in": True}}
            )
            return "Doctor login successful"


        patient_data = patients_collection.find_one({"contact.email": email, "password": password})
        if patient_data:
            patients_collection.update_one(
                {"contact.email": email},
                {"$set": {"_is_logged_in": True}}
            )
            return "Patient login successful"

        raise ValueError("Invalid email or password")

    def book_appointment(self, patient_id:str, doctor_email:str, date_time=None):
        appointment = Appointment(patient_id, doctor_email, date_time)
        collections["appointments"].insert_one(appointment.to_dict())
        return appointment


