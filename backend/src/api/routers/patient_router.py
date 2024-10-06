from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

from src.infraestructure.dto.patient_dto import PatientDTO, PatientCreateDTO
from src.infraestructure.mappers.patient_mapper import (
    map_patient_dto_to_patient_model,
    map_patient_model_to_patient_dto
)
from src.infraestructure.repositories.patient_repository_impl import PatientRepositoryImplementation
from src.infraestructure.database.session import get_db
from src.application.services.patient_service import PatientService

patient_router = APIRouter()

@patient_router("/", status_code=status.HTTP_201_CREATED)
def create_patient(
    patient_request: PatientCreateDTO,
    db: Session = Depends(get_db)
) -> PatientDTO:
    service = PatientService(PatientRepositoryImplementation(db))
    return service.create_patient()