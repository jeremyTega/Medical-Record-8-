from config.database import get_database
from medical_application.appointment import Appointment
from medical_application.diagnosis_entry import DiagnosisEntry
from medical_application.medical_history import MedicalHistory

collections = get_database()
doctors_collection = collections["doctors"]
patients_collection = collections["patients"]
appointments_collection = collections["appointments"]
requested_collection = collections["request_appointments"]
confirmed_collection = collections["appointments"]
records_collection = collections["records"]
patient_collection = collections["patients"]

from medical_application.doctor import Doctor
from medical_application.patient import Patient
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

    def create_patient(self, name, gender , password, my_Contact):
        validate_non_empty("Name", name)
        validate_non_empty("Password", password)
        validate_non_empty("Contact", my_Contact)
        validate_email_format(my_Contact.email)
        patient = Patient(name, gender, password, my_Contact)
        result = patient_collection.insert_one(patient.to_dict())
        return patient


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

    def logout_user(email: str) -> str:
        result = doctors_collection.update_one(
            {"contact.email": email},
            {"$set": {"_is_logged_in": False}}
        )
        if result.modified_count:
            return "Doctor logged out successfully."

        result = patients_collection.update_one(
            {"contact.email": email},
            {"$set": {"_is_logged_in": False}}
        )
        if result.modified_count:
            return "Patient logged out successfully."

        raise ValueError("User not found or already logged out.")


    def book_appointment(self, patient_id:str, doctor_email:str, reason:str, appointment_date:str ):
        appointment = Appointment(patient_id, doctor_email,reason, )
        collections["appointments"].insert_one(appointment.to_dict())
        return appointment

    def get_all_doctors(self):
        doctors = doctors_collection.find({}, {
            "name": 1,
            "specialisation": 1,
            "contact.email": 1

        })
        return list(doctors)

    def approve_appointment(self, appointment_id: str, appointment_date: str):
        requested_appointment = requested_collection.find_one({"appointment_id": appointment_id})
        if not requested_appointment:
            raise ValueError("Invalid appointment id")
        requested_appointment["status"] = "approved"
        requested_appointment["appointment_date"] = appointment_date
        confirmed_collection.insert_one(requested_appointment)
        requested_collection.delete_one({"appointment_id": appointment_id})

        return requested_appointment


    def add_diagnosis(self, patient_email: str, diagnosis_type: str, medication: str):
        if not patient_email or not diagnosis_type or not medication:
            raise ValueError("All fields are required.")

        diagnosis_data = DiagnosisEntry(diagnosis_type, medication).to_dict()

        record = {
            "patient_email": patient_email,
            **diagnosis_data
        }

        records_collection.insert_one(record)
        return record


    def get_medical_records(self, patient_email: str):
        if not patient_email:
            raise ValueError("Patient email is required")

        records_cursor = records_collection.find({"patient_email": patient_email})
        return list(records_cursor)



