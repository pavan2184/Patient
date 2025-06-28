from fastapi import FastAPI
from models import PatientCreate
import database

app = FastAPI()

@app.post("/patients")
def add_patient(patient: PatientCreate):
    return database.create_patient(patient)

@app.get("/patients")
def list_patients():
    return database.get_all_patients()

@app.get("/patients/{pid}")
def get_patient(pid: str):
    patient = database.get_patient_by_id(pid)
    if patient:
        return patient
    return {"message": "Patient not found"}

@app.put("/patients/{pid}")
def update_patient(pid: str, updated_data: PatientCreate):
    updated_patient = database.update_patient(pid, updated_data)
    if updated_patient:
        return updated_patient
    return {"message": "Patient not found"}

@app.delete("/patients/{pid}")
def delete_patient(pid: str):
    deleted = database.delete_patient(pid)
    if deleted:
        return {"message": "Patient deleted successfully"}
    return {"message": "Patient not found"}
