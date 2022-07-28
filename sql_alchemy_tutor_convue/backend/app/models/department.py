from sqlalchemy import Column, Integer, String, func, select, text
from sqlalchemy.orm import column_property, relationship
from connection import Base

from app.models.worker import Worker

class Department(Base):
    __tablename__ = 'departments'
 
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    street = Column(String)
    city = Column(String)
    postcode = Column(String)
 
    workers_no = column_property(
    select(func.count(Worker.pesel)).
    where(Worker.department_id == id).
    select_from(Worker).
    correlate_except(Worker).
    scalar_subquery())

    workers = relationship("Worker", cascade = "all, delete, delete-orphan")