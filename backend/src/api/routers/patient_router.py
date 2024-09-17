from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from typing import List
from ...infraestructure.dto import patient_dto as patient_schema
from ...infraestructure.database.session import SessionLocal
from ...infraestructure.entities.models import Patient as model
from src.infraestructure.database.session import get_db

patient_router = APIRouter()

@patient_router.get("/", response_model=List[patient_schema.Patient], status_code=status.HTTP_200_OK)
def get_all_patients(
    db: Session = Depends(get_db)
) -> List[patient_schema.Patient]:
    patients = db.query(model).all()
    return patients

@patient_router.get("/{patient_id}", response_model=patient_schema.Patient, status_code=status.HTTP_200_OK)
def get_patient_by_id(
    patient_id: int,
    db: Session = Depends(get_db)
):
    patient = db.query(model).filter_by(id=patient_id).first()
    return patient  

@patient_router.post("/", response_model=patient_schema.Patient, status_code=status.HTTP_201_CREATED)
def create_patient(
    input: patient_schema.Patient,
    db: Session = Depends(get_db)
):
    patient = model(
        name = input.name,
        age = input.age,
        gender = input.gender,
        date_birth = input.date_birth,
        city_origin = input.city_origin,
        date_registration = input.date_registration,
        hospital_origin = input.hospital_origin,
        tutor_name = input.tutor_name,
        tutor_phone = input.tutor_phone
    )
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient

@patient_router.put("/{patient_id}", response_model=patient_schema.Patient, status_code=status.HTTP_200_OK)
def update_patient_name_by_id(
    patient_id: int,
    input: patient_schema.PatientUpdateName,
    db: Session = Depends(get_db)
):
    patient = db.query(model).filter_by(id=patient_id).first()
    patient.name = input.name
    db.commit()
    db.refresh(patient)
    return patient

@patient_router.delete("/{patient_id}", response_model=patient_schema.Response)
def delete_patient_by_id(
    patient_id: int,
    db: Session = Depends(get_db)
):
    patient = db.query(model).filter_by(id=patient_id).first()
    db.delete(patient)
    db.commit()
    response = patient_schema.Response(mensaje="Paciente eliminado correctamente")
    return response