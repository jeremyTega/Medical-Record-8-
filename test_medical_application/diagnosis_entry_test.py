import unittest

from medical_application.diagnosis_entry import DiagnosisEntry


class MyTestCase(unittest.TestCase):
    def test_medicalRecordsToStringMethod(self):
        entry = DiagnosisEntry('malaria','malaria meds')
        self.assertEqual('Diagnosis: malaria \n'
                                    'Medication: malaria meds\n'
                                    'Date: 25/07/2025',entry.__str__())


if __name__ == '__main__':
    unittest.main()
