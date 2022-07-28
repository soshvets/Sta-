from connection import *
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean
from sqlalchemy.dialects.postgresql import ARRAY, JSONB


class Salary(Base):
    __tablename__ = 'salary'
 
    id = Column(Integer, primary_key=True, index=True)
    worker_pesel = Column(String, ForeignKey("workers.pesel"))
    month = Column(Integer)
    amount = Column(Integer)

    worker = relationship("Worker", back_populates = "owner_w", cascade = "all, delete")

    


 