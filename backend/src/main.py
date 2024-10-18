from contextlib import asynccontextmanager

from fastapi import FastAPI

from starlette.responses import RedirectResponse
from src.database.management import migrate_tables
from src.routers.patient_router import patient_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application startup")
    migrate_tables()
    yield
    print("Application shutdown")

migrate_tables()

app = FastAPI(
    title="Hospital Patients API",
    summary="API for patient management in a hospital",
    version="1.0.0",
    contact={
        "name": "Ruben Alvarado",
        "email": "ruben_aalvarado@outlook.com"
    },
)

app.include_router(patient_router, prefix="/patients", tags=["Patient"])

@app.get("/")
def main():
    return RedirectResponse(url="/docs")
