from config.database import get_database
collections = get_database()

doctors_collection = collections["doctors"]
patients_collection = collections["patients"]

def validate_non_empty(field_name: str, value):
    if value is None or str(value).strip() == "":
        raise ValueError(f"{field_name} cannot be empty")

def validate_email_format(email: str):
    import re
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValueError("Invalid email format")

def validate_password_strength(password: str):
    if len(password) < 5:
        raise ValueError("Password must be at least 6 characters long")


def is_user_logged_in(email: str) -> bool:
    doctor = doctors_collection.find_one({"contact.email": email})
    if doctor:
        return doctor.get("_is_logged_in", False)

    patient = patients_collection.find_one({"contact.email": email})
    if patient:
        return patient.get("_is_logged_in", False)

    raise ValueError("User not found.")
