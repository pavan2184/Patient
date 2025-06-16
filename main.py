from fastapi import FastAPI
from models import Patient, PatientCreate
import database

app = FastAPI()

@app.post("/patients", response_model=Patient)
def add_patient(patient: PatientCreate):
    return database.create_patient(patient)


@app.get("/patients", response_model=list[Patient])
def list_patients():
    return database.get_all_patients()


@app.get("/patients/{pid}", response_model=Patient | dict)
def get_patient(pid: str):
    patient = database.get_patient_by_id(pid)
    if patient:
        return patient
    return {"message": "Patient not found"}
