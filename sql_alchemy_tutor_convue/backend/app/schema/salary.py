from pydantic import BaseModel

class Salary(BaseModel):
    id: int
    worker_pesel: str
    month: int
    amount: int

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True
