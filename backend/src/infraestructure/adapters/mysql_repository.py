from sqlalchemy.orm import Session
from domain.models.patient_model import Patient
from domain.repositories.patient_repository import PatientRepository
from infraestructure.database.patient_schema import Patient

class PatientMySQLRepository(PatientRepository):
    def __init__(self, db: Session):
        self.db = db

    