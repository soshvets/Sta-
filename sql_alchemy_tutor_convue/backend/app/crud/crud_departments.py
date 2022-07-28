from sqlalchemy.orm import Session
from sqlalchemy import func, update, delete

from typing import List, Dict, Any, Optional

import app.models as models
import app.schema  as schema

class CRUDDepartment:
    '''
        Departments facade
    '''
    def get_all(self, db: Session, q: str,skip: int= 0, limit: int = 100) -> List[schema.Department]:
        '''
        Get all departments
 
        Parameters:
        q - Search by name
        '''
        items = db.query(models.Department).filter(models.Department.name.like(q)).offset(skip).limit(limit).all()
        return items
    
    def get_departments(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Department).offset(skip).limit(limit).all()


    def get(self, db: Session, department_id: int) -> schema.Department:
        item = db.query(models.Department).get(department_id)
        return item

    
    def count(self, db: Session, q: str) -> int:
        return db.query(models.Department.id).filter(models.Department.name.like(q)).count()

    def create_department (self, db: Session, data: schema.DepartmentCreate) -> schema.Department:
        new_department = models.Department()
        new_department.name = data.name
        new_department.street = data.street
        new_department.city = data.city
        new_department.postcode = data.postcode 
        
        db.add(new_department)
        db.commit()
        db.refresh(new_department)

        return new_department


   
    def update(self, db: Session, data: models.Department ) -> schema.Department:
        db.query(models.Department).filter(models.Department.id == data.id).update
        (
            {"name": data.name},
            {"street": data.street},
            {"city": data.city},
            {"postcode": data.postcode},
        )
        db.commit()    

    def update_department(self, db: Session, data: schema.DepartmentBase)  -> schema.DepartmentBase:
        dep = db.query(models.Department).filter(models.Department.id == data.id).one()
        dep.name = data.name
        dep.street = data.street
        dep.city = data.city
        dep.postcode = data.postcode
        
        db.commit()
        updated = db.query(models.Department).filter(models.Department.id == data.id).one()
        return updated
    # def delete(self, db: Session, department_id: int) -> bool:
    #     try:
    #       db.query(models.Department).filter(models.Department.id == department_id).delete()
    #       db.commit()
    #       return True
    #     except:
    #       return False


    def delete(self, db:Session, department_id: int) -> bool:
        department = db.query(models.Department).get(department_id)
        print(type(department))

        if department:
            # db.begin()
            db.delete(department)
            db.commit()
        return True


    def add_worker(self, db: Session, department_id: int, worker_pesel: str) -> bool:
        db.query(models.Worker).filter(models.Worker.pesel == worker_pesel).update(
            {"department_id": department_id}
        )

        db.commit()
        return True
       


    def delete_worker(self, db: Session, department_id: int, worker_pesel: str) -> bool:
        worker = db.query(models.Worker).filter(models.Worker.department_id ==
                                        department_id, models.Worker.pesel == worker_pesel).one()
        if worker:
            worker.department_id = None
            db.commit()
            return True


 