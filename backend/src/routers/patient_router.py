from typing import List
from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

from src.models.patient_model import Patient as patient_model
from src.schemas import patient_schema
from src.database.connection import get_db
from src.mappers.patient_mapper import map_schema_to_model

patient_router = APIRouter()

@patient_router.post(
        "/",
        status_code=status.HTTP_201_CREATED,
        response_model=patient_schema.Patient
)
async def create_patient(
    patient: patient_schema.Patient,
    db: Session = Depends(get_db)
):
    patient = patient_model(
        name = patient.name,
        age = patient.age,
        gender = patient.gender,
        birth_date = patient.birth_date,
        city_origin = patient.city_origin,
        registration_date = patient.registration_date,
        hospital_origin = patient.hospital_origin,
        tutor_name = patient.tutor_name,
        tutor_phone = patient.tutor_phone
    )

    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient

@patient_router.get(
        "/",
        status_code=status.HTTP_200_OK,
        response_model=List[patient_schema.Patient]
)
async def get_all_patients(
    db: Session = Depends(get_db)
):
    patients = db.query(patient_model).all()
    return patients

@patient_router.get(
        "/{patient_id}",
        status_code=status.HTTP_200_OK,
        response_model=patient_schema.Patient
)
async def get_patient_by_patient_id(
    patient_id: int,
    db: Session = Depends(get_db)
):
    patient = db.query(patient_model).filter_by(id=patient_id).first()
    
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@patient_router.put(
        "/{patient_id}",
        status_code=status.HTTP_200_OK,
        response_model=patient_schema.Patient
)
async def update_patient(
    patient_id: int,
    patient_info: patient_schema.Patient,
    db: Session = Depends(get_db)
):
    patient = db.query(patient_model).filter_by(id = patient_id).first()
    
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    patient.name = patient_info.name
    patient.age = patient_info.age
    patient.gender = patient_info.gender
    patient.birth_date = patient_info.birth_date
    patient.city_origin = patient_info.city_origin
    patient.registration_date = patient_info.registration_date
    patient.hospital_origin = patient_info.hospital_origin
    patient.tutor_name = patient_info.tutor_name
    patient.tutor_phone = patient_info.tutor_phone
    
    db.commit()
    db.refresh(patient)
    return patient

@patient_router.delete(
        "/{patient_id}",
        status_code=status.HTTP_200_OK,
        response_model=patient_schema.Patient
)
async def delete_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):
    patient = db.query(patient_model).filter_by(id=patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    db.delete(patient)
    db.commit()
    return patient