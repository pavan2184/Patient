from pydantic import BaseModel, Field
from datetime import datetime

class PatientCreate(BaseModel):
    name: str
    age: int
    condition: str
    created_at: datetime

class Patient(PatientCreate):
    id: str 
    

