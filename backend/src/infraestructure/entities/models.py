from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from ..database.session import Base

class Patient(Base):
    __tablename__ = 'patient'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200))
    age = Column(Integer)
    gender = Column(String(20))
    date_birth = Column(DateTime())
    city_origin = Column(String(200))
    date_registration = Column(DateTime, default=datetime.now())
    hospital_origin = Column(String(200))
    tutor_name = Column(String(200))
    tutor_phone = Column(Integer)
