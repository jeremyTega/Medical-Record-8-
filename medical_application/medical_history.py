# from diagnosis_entry import DiagnosisEntry
from medical_application.diagnosis_entry import DiagnosisEntry
class MedicalHistory:
    def __init__(self):
        self.entries: list[DiagnosisEntry] = []

    def add_entry(self,diagnosis_type:str,medication:str):
        for entry in self.entries:
            if diagnosis_type == entry.get_diagnosis_type():
                raise ValueError("Diagnosis type already registered")
        entry = DiagnosisEntry(diagnosis_type,medication)
        self.entries.append(entry)
    def find_entry(self,diagnosis_type:str):
        for entry in self.entries:
            if diagnosis_type == entry.get_diagnosis_type():
                return entry
        raise ValueError("Entry not found")
    def remove_entry(self,diagnosis_type:str):
        for entry in self.entries:
            if diagnosis_type == entry.get_diagnosis_type():
                self.entries.remove(entry)
                return
        raise ValueError("Entry not found")
    def get_entries(self):
        return self.entries