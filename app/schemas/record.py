from pydantic import BaseModel,validator
from datetime import date
class RecordCreate(BaseModel):
    amount: float
    type: str
    category: str
    date: date
    notes: str | None = None
    @validator("type")
    def validate_type(cls,v):
        if v not in ["income","expense"]:
            raise ValueError("Type must be income or expense")
        return v
    
    class RecordOut(BaseModel):
        id:int 
        amount:float
        type:str
        category:str 
        
        class Config:
            from_attributes = True
            