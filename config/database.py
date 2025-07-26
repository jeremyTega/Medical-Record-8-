from pymongo import MongoClient


def get_database():
    uri = "mongodb+srv://oghenedemartin:cvQCKBHtcjLmSuoH@medicalsystem.xb62ss8.mongodb.net/?retryWrites=true&w=majority&appName=medicalSystem"

    client = MongoClient(uri)
    db = client["medical_db"]

    collections = {
        "doctors": db["doctors"],
        "patients": db["patients"],
        "records": db["records"]
    }
    return collections