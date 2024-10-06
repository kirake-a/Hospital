from typing import List
from fastapi import Depends

from sqlalchemy.orm import Session
from sqlalchemy import select

from src.infraestructure.mappers.patient_mapper import (
    map_patient_entity_to_patient_model,
    map_patient_model_to_patient_entity
)
from src.infraestructure.entities.patient_entity import Patient
from src.application.repositories.patient_repository import PatientRepository
from src.domain.models.patient_model import PatientModel

class PatientRepositoryImplementation(PatientRepository):
    def __init__(
            self,
            db: Session
    ):
        self.db = db

    def create_patient(self, patient: PatientModel) -> PatientModel:
        # If id, try to find patient in db
        if patient.id:
            patient_entity = self.db.execute(
                select(Patient).where(Patient.id == patient.id)
            ).scalars().first()
        else:
            patient_entity = None

        if patient_entity:
            # Updating registry
            patient_entity.name = patient.name
            patient_entity.age = patient.age
            patient_entity.gender = patient.gender
            patient_entity.date_birth = patient.date_birth
            patient_entity.city_origin = patient.city_origin
            patient_entity.date_registration = patient.date_registration
            patient_entity.hospital_origin = patient.hospital_origin
            patient_entity.tutor_name = patient.tutor_name
            patient_entity.tutor_phone = patient.tutor_phone
        else:
            patient_entity = map_patient_model_to_patient_entity(patient)    
            self.db.add(patient_entity)
            
        # Saving changes  
        self.db.commit()
        self.db.refresh(patient_entity)
        return map_patient_entity_to_patient_model(patient_entity)
    
    def get_patient_by_id(self, patient_id: int) -> PatientModel | None:
        patient_entity = self.db.query(Patient).filter_by(id=patient_id).first()
        
        if patient_entity:
            return map_patient_entity_to_patient_model(patient_entity)
        else:
            return None
    
    def get_all_patients(self) -> List[PatientModel]:
        patients_entity = self.db.query(Patient).all()

        return [
            map_patient_entity_to_patient_model(patient) for patient in patients_entity
        ]
    
    def update_patient(self, patient: PatientModel) -> PatientModel:
        raise NotImplementedError(
            "Method has not been implemented yet."
        )
    
    def delete_patient_by_id(self, patient_id) -> PatientModel:
        patient_entity = self.db.query(Patient).filter_by(id=patient_id).first()
        self.db.delete(patient_entity)
        self.db.commit()

        return map_patient_entity_to_patient_model(patient_entity)
