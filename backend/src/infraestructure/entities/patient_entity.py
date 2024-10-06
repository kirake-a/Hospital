from sqlalchemy import Column, Integer, String, DateTime, Date
from datetime import datetime
from src.infraestructure.database.session import Base

class Patient(Base):
    __tablename__ = 'patient'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(20), nullable=False)
    date_birth = Column(Date(), nullable=False)
    city_origin = Column(String(200), nullable=False)
    date_registration = Column(DateTime, default=datetime.now(), nullable=False)
    hospital_origin = Column(String(200), nullable=False)
    tutor_name = Column(String(200), nullable=False)
    tutor_phone = Column(Integer, nullable=False)
