from src.schemas.patient_schema import Patient as patient_schema
from src.models.patient_model import Patient as patient_model

def map_schema_to_model(
        input: patient_schema
) -> patient_model:
    return patient_model(
        name = input.name,
        age = input.age,
        gender = input.gender,
        birth_date = input.birth_date,
        city_origin = input.city_origin,
        registration_date = input.registration_date,
        hospital_origin = input.hospital_origin,
        tutor_name = input.tutor_name,
        tutor_phone = input.tutor_phone
    )