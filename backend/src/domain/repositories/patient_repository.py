from abc import ABC, classmethod
from typing import List, Optional
from domain.models.patient_model import Patient

class PatientRepository(ABC):
    @classmethod
    def create_patient(self, patient: Patient) -> Patient:
        pass

    @classmethod
    def get_patient_by_id(self, patient_id: int) -> Optional[Patient]:
        pass

    @classmethod
    def get_all_patients(self) -> List[Patient]:
        pass

    @classmethod
    def delete_patient_by_id(self, patient_id: int) -> bool:
        pass

# Revisar esta implementacion
    @classmethod
    def update_patient_by_id(self, patient_id: int) -> Patient:
        pass
