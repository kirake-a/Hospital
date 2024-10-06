from typing import List
from src.domain.models.patient_model import PatientModel

class PatientRepository:
    def create_patient(self, patient: PatientModel) -> PatientModel:
        raise NotImplementedError(
            "Method has not been implemented yet."
        )
    
    def get_patient_by_id(self, patient_id: int) -> PatientModel | None:
        raise NotImplementedError(
            "Method has not been implemented yet."
        )
    
    def get_all_patients(self) -> List[PatientModel]:
        raise NotImplementedError(
            "Method has not been implemented yet."
        )
    
    def update_patient(self, patient: PatientModel) -> PatientModel:
        raise NotImplementedError(
            "Method has not been implemented yet."
        )
    
    def delete_patient_by_id(self, patient_id) -> PatientModel:
        raise NotImplementedError(
            "Method has not been implemented yet."
        )
