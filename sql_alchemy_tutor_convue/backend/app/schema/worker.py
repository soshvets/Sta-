from pydantic import BaseModel
from typing import List, Optional

from app.schema.child import Child
from app.schema.salary import Salary
# from app.schema.department import Department

class Worker(BaseModel):
    pesel: str
    name: str
    surname: str
    age: int
    criminal_record: bool
 
    children:   Optional[List[Child]]
    # salary: int 
    owner_w: Optional[ List[Salary]]
    department_id: int
 
    class Config:
        arbitrary_types_allowed = True
        orm_mode = True

class WorkerSimple(BaseModel):
    pesel: str
    name: str
    surname: str
    age: int
 
    class Config:
        orm_mode = True
