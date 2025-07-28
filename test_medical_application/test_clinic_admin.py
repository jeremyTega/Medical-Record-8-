import unittest
from datetime import datetime
from unittest.mock import patch, MagicMock

from medical_application import contact
from medical_application.appointment import Appointment
from medical_application.doctor import Doctor
from users.clinic_admin import Admin
from medical_application.contact import Contact
from medical_application.address import Address
from users.clinic_admin import Admin

class TestAdminCreateDoctor(unittest.TestCase):


    @patch("users.clinic_admin.doctors_collection")
    @patch("users.clinic_admin.patients_collection")
    def test_login_success_doctor(self, mock_patients, mock_doctors):
        admin = Admin("admin")

        mock_doctors.find_one.return_value = {
            "contact": {"email": "doc@example.com"},
            "password": "pass"
        }

        result = admin.login_user("doc@example.com", "pass")

        mock_doctors.update_one.assert_called_once_with(
            {"contact.email": "doc@example.com"},
            {"$set": {"_is_logged_in": True}}
        )

        self.assertEqual(result, "Doctor login successful")

    @patch("users.clinic_admin.doctors_collection")
    @patch("users.clinic_admin.patients_collection")
    def test_login_user_as_patient(self, mock_patients, mock_doctors):
        admin = Admin("admin")

        # Setup doctor not found
        mock_doctors.find_one.return_value = None

        # Setup fake patient return
        mock_patients.find_one.return_value = {
            "contact": {"email": "patient@example.com"},
            "password": "mypassword"
        }

        message = admin.login_user("patient@example.com", "mypassword")
        self.assertEqual(message, "Patient login successful")
        mock_patients.update_one.assert_called_once()

    @patch("users.clinic_admin.confirmed_collection")
    @patch("users.clinic_admin.requested_collection")
    def test_approve_appointment_by_id_success(self, mock_requested, mock_confirmed):
        # Arrange
        address = Address("house_no", "street", "city", "state")
        contact = Contact("phone", "email", address)
        doctor = Doctor("name", "password", "specialisation", contact)

        test_appointment = {
            "appointment_id": "1234",
            "patient_email": "patient@example.com",
            "doctor_email": "doc@example.com",
            "reason": "Checkup",
            "status": "pending"
        }

        # Simulate finding the appointment in the "requested" collection
        mock_requested.find_one.return_value = test_appointment

        # Act
        result = doctor.approve_appointment_by_id("1234", "2025-08-01 10:00 AM")


        self.assertEqual(result["status"], "approved")
        self.assertEqual(result["appointment_date"], "2025-08-01 10:00 AM")

        mock_requested.find_one.assert_called_once_with({"appointment_id": "1234"})
        mock_confirmed.insert_one.assert_called_once_with(test_appointment)
        mock_requested.delete_one.assert_called_once_with({"appointment_id": "1234"})



    # @patch("users.clinic_admin.collections")
    # def test_book_appointment(self, mock_collections):
    #     # Arrange
    #     mock_appointments_collection = MagicMock()
    #     mock_collections.__getitem__.return_value = mock_appointments_collection
    #
    #     admin = Admin("admin_user")
    #     patient_id = "patient123"
    #     doctor_email = "doctor@example.com"
    #     date_time = datetime(2025, 7, 26, 14, 30)
    #
    #     # Act
    #     appointment = admin.book_appointment(patient_id, doctor_email, date_time)
    #
    #     # Assert
    #     self.assertIsInstance(appointment, Appointment)
    #     self.assertEqual(appointment.patient_id, patient_id)
    #     self.assertEqual(appointment.doctor_email, doctor_email)
    #     self.assertEqual(appointment.date_time, date_time)
    #     mock_appointments_collection.insert_one.assert_called_once_with(appointment.to_dict())

    # @patch("your_module.get_database")
    # def test_login_failure(self, mock_get_db):
    #             mock_doctors = MagicMock()
    #             mock_patients = MagicMock()
    #             mock_get_db.return_value = {
    #                 "doctors": mock_doctors,
    #                 "patients": mock_patients
    #             }
    #
    #             # Simulate no match
    #             mock_doctors.find_one.return_value = None
    #             mock_patients.find_one.return_value = None
    #
    #             with self.assertRaises(ValueError) as context:
    #                 Admin.login_user("unknown@example.com", "wrongpass")
    #
    #             self.assertEqual(str(context.exception), "Invalid email or password")
    # @patch("users.clinic_admin.Admin.book_appointments")
    # def test_book_appointment(self):


if __name__ == "__main__":
    unittest.main()
