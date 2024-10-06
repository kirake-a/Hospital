from pydantic import BaseModel
from datetime import datetime

# Create and update patient
class PatientBase(BaseModel):
    name: str
    age: int
    gender: str
    date_birth: datetime
    city_origin: str
    hospital_origin: str
    tutor_name: str
    tutor_phone: int

# Create a new patient
class PatientCreate(PatientBase):
    pass

# Read patient
class Patient(PatientBase):
    id: int
    date_registration: datetime

    class Config:
        from_attributes = True

class PatientUpdateName(BaseModel):
    name: str

    class Config:
        from_attributes = True

class Response(BaseModel):
    mensaje: str