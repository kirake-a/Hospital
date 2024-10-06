from typing import List
from src.domain.models.patient_model import PatientModel
from src.application.repositories.patient_repository import PatientRepository
from src.domain.exceptions.ConflictWithExistingResourceException import (
    ConflictWithExistingResourceException
)
from src.domain.exceptions.ResourceNotFoundException import ResourceNotFoundException

class PatientService:
    def __init__(
            self,
            patient_repository: PatientRepository
    ) -> None:
        self.patient_repository = patient_repository

    def create_patient(self, patient: PatientModel) -> PatientModel:
        if self.patient_repository.create_patient(patient):
            raise ConflictWithExistingResourceException
        return self.patient_repository.create_patient(patient)
    
    def get_patient_by_id(self, patient_id: int) -> PatientModel | None:
        if patient := self.patient_repository.get_patient_by_id(patient_id):
            return patient
        raise ResourceNotFoundException
    
    def get_all_patients(self) -> List[PatientModel]:
        return self.patient_repository.get_all_patients()
        
    
    def update_patient(self, patient: PatientModel) -> PatientModel:
        if not patient.id or not self.patient_repository.get_patient_by_id(
            patient.id
        ):
            raise ResourceNotFoundException
        return self.patient_repository.create_patient(patient)
        
    
    def delete_patient_by_id(self, patient_id) -> None:
        if not self.get_patient_by_id(patient_id):
            raise ResourceNotFoundException
        return self.patient_repository.delete_patient_by_id(patient_id)