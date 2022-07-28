from typing import Optional, Any, List
from pydantic import BaseModel

from app.schema.worker import Worker, WorkerSimple

class DepartmentBase(BaseModel):
    id: int
    name: str
    street: str
    city: str
    postcode: str

    class Config:
        orm_mode = True
        # arbitrary_types_allowed = True

class DepartmentCreate(DepartmentBase):
    pass

class Department(DepartmentBase):
    id: int
    workers_no: int = 0
    workers: List[WorkerSimple] = []