from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# Para probar
#from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

DATABASE_URL = 'mysql+mysqlconnector://root:password@localhost:3306/hospital'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()