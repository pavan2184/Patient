from pydantic import BaseModel, Field
from datetime import datetime

class PatientCreate(BaseModel):
    name: str
    age: int
    condition: str

class Patient(PatientCreate):
    id: str 
    created_at: int = Field(default_factory=lambda: int(datetime.timestamp(datetime.now())))

