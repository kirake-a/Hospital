from fastapi import Depends
from src.schemas import patient_schema
from sqlalchemy.orm import Session
from src.database.connection import get_db
from src.models.patient_model import Patient as patient_model

class PatientService:

    def __init__(self) -> None:
        self.db: Session = get_db

    def create_patient(
            patient: patient_schema
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

        self.db.add(patient)
        self.db.commit()
        self.db.refresh(patient)
        return patient