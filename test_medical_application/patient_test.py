import unittest
from unittest.mock import patch
import mongomock

from medical_application.Patient.patient import Patient
from medical_application.contact import Contact
from medical_application.address import Address
from medical_application.appointment import Appointment


class TestPatient(unittest.TestCase):

    def setUp(self):
        self.mock_db = mongomock.MongoClient().db
        self.mock_db.create_collection("requested_appointment")

        self.address = Address("12", "Baker St", "Lagos", "Lagos")
        self.contact = Contact("08012345678", "john@example.com", self.address)
        self.patient = Patient("John Doe", "male", "secret", self.contact, db=self.mock_db)

    def test_request_appointment_inserts_into_db(self):
        self.patient.request_appointment("john@example.com", "doc@example.com", "Flu symptoms")

        inserted = self.mock_db["request_appointment"].find_one({"patient_id": "john@example.com"})
        self.assertIsNotNone(inserted)
        self.assertEqual(inserted["doctor_email"], "doc@example.com")
        self.assertEqual(inserted["reason"], "Flu symptoms")

        self.patient.request_appointment("john@example.com", "doc2@example.com", "fever")
        appointments = list(self.mock_db["request_appointment"].find({"patient_id": "john@example.com"}))
        self.assertEqual(len(appointments), 2)
        self.assertEqual(appointments[0]["doctor_email"],"doc@example.com")
        self.assertEqual(appointments[0]["reason"], "Flu symptoms")
        self.assertEqual(appointments[1]["doctor_email"],"doc2@example.com")
        self.assertEqual(appointments[1]["reason"], "fever")


    def test_add_appointment_adds_to_list(self):
        appt = Appointment("john@example.com", "doc@example.com", "Checkup")
        self.patient.add_appointment(appt)

        self.assertEqual(len(self.patient.get_appointments()), 1)
        self.assertEqual(self.patient.get_appointments()[0].reason, "Checkup")

    def test_to_dict_serializes_patient(self):
        result = self.patient.to_dict()
        self.assertEqual(result["name"], "John Doe")
        self.assertEqual(result["contact"]["email"], "john@example.com")
        self.assertEqual(result["contact"]["address"]["city"], "Lagos")
        self.assertFalse(result["_is_logged_in"])
        self.assertEqual(result["role"], "patient")

    def test_getters_return_correct_values(self):
        self.assertEqual(self.patient.get_address().city, "Lagos")
        self.assertEqual(self.patient.get_contact().email, "john@example.com")
        self.assertEqual(self.patient.get_password(), "secret")
        self.assertFalse(self.patient.is_logged())


if __name__ == "__main__":
    unittest.main()
