from connection import *
from sqlalchemy.orm import relationship, column_property
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, select, func
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
from app.models.salary import Salary


class Worker(Base):
    __tablename__ = 'workers'

    pesel = Column(String, primary_key=True)
    name = Column(String)
    surname = Column(String)
    age = Column(Integer)
    criminal_record= Column(Boolean)
    children=Column(JSONB, default=dict())
    department_id = Column(Integer, ForeignKey("departments.id"))
    

    # salary = column_property(select(func.sum(Salary.amount)).where(Salary.worker_pesel == pesel).scalar_subquery())


   
    # owner = relationship('Department', back_populates='worker')
    owner_w = relationship('Salary', back_populates='worker')

    # def __repr__(self):
    #     return f'{self.pesel} | {self.name} {self.surname} {self.age} {self.criminal_record} {self.children} {self.department_id}'
