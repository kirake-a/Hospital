from sqlalchemy.orm import Session
from domain.models.patient_model import PatientModel
from src.application.repositories.patient_repository import PatientRepository
from src.infraestructure.database.patient_schema_db import Patient

class PatientMySQLRepository(PatientRepository):
    def __init__(self, db: Session):
        self.db = db

    