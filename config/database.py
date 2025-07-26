from pymongo import MongoClient


uri = "mongodb+srv://oghenedemartin:cvQCKBHtcjLmSuoH@medicalsystem.xb62ss8.mongodb.net/?retryWrites=true&w=majority&appName=medicalSystem"


client = MongoClient(uri)


db = client["medical_db"]
doctors_collection = db["doctors"]


doctor = {
    "name": "Dr. John Doe",
    "password": "securepass",
    "specialisation": "Cardiologist",
    "contact": {
        "name": "Dr. John",
        "phone_no": "08012345678",
        "email": "john@example.com",
        "address": {
            "house_no": "12",
            "street": "Health Ave",
            "city": "Lagos",
            "state": "Lagos"
        }
    }
}


result = doctors_collection.insert_one(doctor)

print("Doctor inserted with _id:", result.inserted_id)
