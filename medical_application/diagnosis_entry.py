from datetime import date


def validate_str_input(string:str):
    if string is None:
        raise ValueError(f'{string} cannot be None')
    if type(string) is not str:
        raise ValueError(f'{string} must be a string')
    if string.strip() == "":
        raise ValueError(f'{string} cannot be empty')

class DiagnosisEntry:
    def __init__(self,diagnosis_type:str,medication:str):
        self.diagnosis_type = diagnosis_type
        self.medication = medication
        self.date = date.today()

    def set_diagnosis_type(self,diagnosis_type:str):
        validate_str_input(diagnosis_type)
        self.diagnosis_type = diagnosis_type
    def get_diagnosis_type(self):
        return self.diagnosis_type

    def set_medication(self,medication:str):
        validate_str_input(medication)
        self.medication = medication
    def get_medication(self):
        return self.medication

    def get_date(self):
        return self.date.strftime('%d/%m/%Y').strip()

    def __str__(self):
        return (f'Diagnosis: {self.get_diagnosis_type()} \n'
                f'Medication: {self.get_medication()}\n'
                f'Date: {self.get_date()}')

    def to_dict(self):
        return {
            "diagnosis_type": self.diagnosis_type,
            "medication": self.medication,
            "date": self.date.isoformat()
        }