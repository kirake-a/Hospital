from typing import List
from fastapi import Depends, FastAPI, HTTPException
from starlette.responses import RedirectResponse
from sqlalchemy.orm import Session
from src.infraestructure import schemas
from src.infraestructure.database.session import engine
#from src.api.routers.patient_router_old import patient_router
from src.api.routers.patient_router import patient_router
from src.infraestructure.entities import patient_entity

patient_entity.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(
    patient_router, prefix="/patient", tags=["Patient"]
)

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")
