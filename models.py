from pydantic import BaseModel, Field
from datetime import datetime

class Patient(BaseModel):
    name: str
    age: int
    condition: str
    created_at: int = Field(default_factory=lambda: int(datetime.timestamp(datetime.now())))
    updated_at: int = Field(default_factory=lambda: int(datetime.timestamp(datetime.now())))
