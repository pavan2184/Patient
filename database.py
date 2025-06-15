from pymongo import MongoClient
from bson import ObjectId
from models import Patient,PatientCreate
from datetime import datetime


client = MongoClient("mongodb://localhost:27017")
db = client.patientdb
collection = db.patients


def convert(patient):
    return {
        "id": str(patient["_id"]),
        "name": patient["name"],
        "age": patient["age"],
        "condition": patient["condition"],
        "created_at": int(patient["created_at"].timestamp()) 
    }



def create_patient(data):
    doc = data.dict()
    doc["created_at"] = datetime.utcnow()
    result = collection.insert_one(doc)
    patient = collection.find_one({"_id": result.inserted_id})
    return convert(patient)

def get_all_patients():
    return [convert(p) for p in collection.find()]


def get_patient_by_id(id):
    patient = collection.find_one({"_id": ObjectId(id)})
    return convert(patient)
    
