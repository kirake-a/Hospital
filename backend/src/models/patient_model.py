from sqlalchemy import Column, Integer, String, Date
from datetime import date
from src.database.connection import Base

# Tabla que se crea en la base de datos
class Patient(Base):
    __tablename__ = 'patient'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(20), nullable=False)
    birth_date = Column(Date(), nullable=False)
    city_origin = Column(String(200), nullable=False)
    registration_date = Column(Date, default=date.today(), nullable=False)
    hospital_origin = Column(String(200), nullable=False)
    tutor_name = Column(String(200), nullable=False)
    tutor_phone = Column(String(13), nullable=False)