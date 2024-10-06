from pydantic import BaseModel
from datetime import datetime, date

# Create and update patient
class PatientBase(BaseModel):
    name: str
    age: int
    gender: str
    date_birth: date
    city_origin: str
    date_registration: datetime
    hospital_origin: str
    tutor_name: str
    tutor_phone: int

class PatientDTO(BaseModel):
    id: int
    name: str
    age: int
    gender: str
    date_birth: date
    city_origin: str
    date_registration: datetime
    hospital_origin: str
    tutor_name: str
    tutor_phone: int

# Create a new patient
class PatientCreateDTO(PatientBase):
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