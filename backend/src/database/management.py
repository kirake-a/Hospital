from src.database.connection import (
    SessionLocal,
    engine,
    Base
)
from src.models import Patient


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

def migrate_tables():
    Base.metadata.create_all(bind=engine)