from src.domain.models.patient_model import PatientModel
from src.infraestructure.dto.patient_dto import PatientDTO
from src.infraestructure.entities.patient_entity import Patient

def map_patient_entity_to_patient_model(
        patient_entity: Patient
) -> PatientModel:
    return PatientModel(
        id = patient_entity.id,
        name = patient_entity.name,
        age = patient_entity.age,
        gender = patient_entity.gender,
        date_birth = patient_entity.date_birth,
        city_origin = patient_entity.city_origin,
        date_registration = patient_entity.date_registration,
        hospital_origin = patient_entity.hospital_origin,
        tutor_name = patient_entity.tutor_name,
        tutor_phone = patient_entity.tutor_phone
    )

def map_patient_model_to_patient_entity(
        patient_model: PatientModel
) -> Patient:
    return Patient(
        id = patient_model.id,
        name = patient_model.name,
        age = patient_model.age,
        gender = patient_model.gender,
        date_birth = patient_model.date_birth,
        city_origin = patient_model.city_origin,
        date_registration = patient_model.date_registration,
        hospital_origin = patient_model.hospital_origin,
        tutor_name = patient_model.tutor_name,
        tutor_phone = patient_model.tutor_phone
    )

def map_patient_dto_to_patient_model(
        patient_dto = PatientDTO
):
    return PatientModel(
        id = patient_dto.id,
        name = patient_dto.name,
        age = patient_dto.age,
        gender = patient_dto.gender,
        date_birth = patient_dto.date_birth,
        city_origin = patient_dto.city_origin,
        date_registration = patient_dto.date_registration,
        hospital_origin = patient_dto.hospital_origin,
        tutor_name = patient_dto.tutor_name,
        tutor_phone = patient_dto.tutor_phone
    )

def map_patient_model_to_patient_dto(
        patient_model = PatientModel
) -> PatientDTO:
    return PatientDTO(
        id = patient_model.id,
        name = patient_model.name,
        age = patient_model.age,
        gender = patient_model.gender,
        date_birth = patient_model.date_birth,
        city_origin = patient_model.city_origin,
        date_registration = patient_model.date_registration,
        hospital_origin = patient_model.hospital_origin,
        tutor_name = patient_model.tutor_name,
        tutor_phone = patient_model.tutor_phone
    )