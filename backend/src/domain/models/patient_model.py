from datetime import datetime
from dataclasses import dataclass

@dataclass
class Patient: 
    id: int
    name: str
    age: str
    gender: str
    date_birth: datetime
    city_origin: str
    hospital_origin: str
    tutor_name: str
    tutor_phone: str