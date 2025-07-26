import unittest

from medical_application.patient import Patient


class MyTestCase(unittest.TestCase):
    def test_that_patient_logs_in_with_correct_credentials(self):
        patient = Patient("firstName LastName", "male","12/08/1980")
        patient.set_password("correctPassword")
        address = patient.set_address(1,"Good health str","Texas","Texas")
        patient.create_contact("firstName LastName","email.@yahoo.com",address)
        patient.log_in("email.@yahoo.com","correctPassword")
        self.assertTrue(patient.is_logged())

    def test_that_errors_are_thrown_when_patient_is_created_with_wrong_details(self):
        with self.assertRaises(ValueError):
            Patient("firstName LastName", "bi-sexual", "12/08/1980")
        with self.assertRaises(ValueError):
            Patient("firstName LastName", "male", "12/08/2029")





if __name__ == '__main__':
    unittest.main()
