from typing import Optional
from pydantic import BaseModel
from datetime import date

class PatientBase(BaseModel):
    name: str
    age: int
    gender: str
    birth_date: date
    city_origin: str
    hospital_origin: str
    tutor_name: str
    tutor_phone: str

class Patient(PatientBase):
    id: Optional[int]
    registration_date: date

    class Config:
        from_attributes = True
