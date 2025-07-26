import unittest
from unittest.mock import patch, MagicMock
from users.clinic_admin import Admin
from medical_application.contact import Contact
from medical_application.address import Address

class TestAdminCreateDoctor(unittest.TestCase):
    def setUp(self):
        self.admin = Admin("admin_user")
        self.contact = Contact(
            name="Dr. Ada",
            phone_no="08012345678",
            email="ada@clinic.com",
            address=Address(house_no="10", street="Broadway", city="Lagos", state="Lagos")
        )

    @patch("medical_application.users.admin.doctors_collection.insert_one")
    def test_create_doctor_successfully(self, mock_insert_one):
        # Arrange: set up mock return
        mock_result = MagicMock()
        mock_result.inserted_id = "some_id"
        mock_insert_one.return_value = mock_result

        # Act: call the method
        doctor = self.admin.create_doctor(
            name="Ada Eze",
            password="strongPass123",
            specialisation="Cardiology",
            my_Contact=self.contact
        )

        # Assert: check that insert_one was called and a Doctor object returned
        self.assertEqual(doctor.name, "Ada Eze")
        self.assertEqual(doctor.specialisation, "Cardiology")
        self.assertEqual(doctor.contact.email, "ada@clinic.com")
        mock_insert_one.assert_called_once()

    def test_create_doctor_invalid_email(self):
        self.contact.email = "not-an-email"
        with self.assertRaises(ValueError) as context:
            self.admin.create_doctor("Ada", "pass123", "Cardio", self.contact)
        self.assertIn("Invalid email format", str(context.exception))

    def test_create_doctor_empty_name(self):
        with self.assertRaises(ValueError) as context:
            self.admin.create_doctor("", "pass123", "Cardio", self.contact)
        self.assertIn("Name cannot be empty", str(context.exception))


if __name__ == "__main__":
    unittest.main()
