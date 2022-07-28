from datetime import date
from pydantic import BaseModel

class Child(BaseModel):
   
    dob: str   #'2019-12-04'
    imie: str
    
    class Config:
        arbitrary_types_allowed = True
        orm_mode = True
