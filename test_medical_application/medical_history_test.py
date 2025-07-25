import unittest

from medical_application.medical_history import MedicalHistory
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.history = MedicalHistory()
    def test_that_entries_can_be_added(self):
        self.history.add_entry("Malaria","Malaria meds")
        self.assertEqual("Malaria",self.history.find_entry("Malaria").diagnosis_type)
    def test_that_entries_can_be_removed(self):
        self.history.add_entry("Malaria","Malaria meds")
        self.history.add_entry("Typhoid","Typhoid meds")
        self.history.remove_entry("Typhoid")
        entries = ['Diagnosis: Malaria \n'
                                    'Medication: Malaria meds\n'
                                    'Date: 25/07/2025']
        st_entries =[str(e) for e in self.history.get_entries()]
        self.assertEqual(entries,st_entries)






if __name__ == '__main__':
    unittest.main()
