import unittest

from medical_application.contact import Contact
from medical_application.address import Address
from medical_application.contact import Contact
from medical_application.doctor import Doctor


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.address = Address("house_no", "street", "city", "state")
        self.contact =Contact("name", "phone", "email", self.address)
        self.doctor = Doctor("name", "correct password", "specialisation", self.contact)

    def test_doctor_sign_up(self):
        myAddress = Address("house_no", "street", "city", "state")
        my_Contact = Contact("name","phone", "email", myAddress)
        new_doctor = Doctor.sign_up("name", "correct password", "specialisation", my_Contact)
        self.assertEqual(new_doctor.name, "name")
        self.assertEqual(new_doctor.contact.email, "email")

    def test_that_doctor_signup_without_contact_throws_value_error(self):
        with self.assertRaises(ValueError) as context:
            Doctor.sign_up("name", "correct password", "specialisation", None)
        self.assertEqual(str(context.exception), "Contact cannot be None")

    def test_that_doctor_signup_without_password_throws_value_error(self):
        with self.assertRaises(ValueError) as context:
            Doctor.sign_up("name", None, "specialisation", self.contact)
        self.assertEqual(str(context.exception), "Password cannot be None")

    def test_that_doctor_can_login(self):
        myAddress = Address("house_no", "street", "city", "state")
        my_Contact = Contact("name", "phone", "email", myAddress)

        new_doctor = Doctor.sign_up("name", "correct password", "specialisation", my_Contact)

        self.assertEqual(new_doctor.name, "name")
        logged_in_doctor = Doctor.log_in(my_Contact.email, "correct password")
        self.assertTrue(logged_in_doctor.is_logged_in)


if __name__ == '__main__':
    unittest.main()
