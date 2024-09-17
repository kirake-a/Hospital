from typing import List, Optional
from domain.repositories.patient_repository import PatientRepository
from domain.models.patient_model import Patient

class DriverService:
    def __init__(self, repository: PatientRepository):
        self.repository = repository

    def create_patient(self, patient: Patient) -> Patient:
        return self.repository.create_patient(patient)

    def get_patient_by_id(self, patient_id: int) -> Optional[Patient]:
        return self.repository.get_patient_by_id(patient_id)
    
    def get_all_patients(self) -> List[Patient]:
        return self.repository.get_all_patients(self)
    
    def delete_patient_by_id(self, patient_id: int) -> bool:
        return self.repository.delete_patient_by_id(patient_id)