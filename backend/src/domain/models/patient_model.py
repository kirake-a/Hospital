from datetime import date, datetime

class PatientModel:
    def __init__(
            self,
            id: int | None,
            name: str,
            age: str,
            gender: str,
            date_birth: date,
            city_origin: str,
            date_registration: datetime,
            hospital_origin: str,
            tutor_name: str,
            tutor_phone: str
    ):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.date_birth = date_birth
        self.city_origin = city_origin
        self.date_registration = date_registration
        self.hospital_origin = hospital_origin
        self.tutor_name = tutor_name
        self.tutor_phone = tutor_phone