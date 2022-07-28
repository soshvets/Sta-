import json
from sqlalchemy.orm import Session
from sqlalchemy import func

from typing import List, Dict, Any, Optional
from sqlalchemy.orm.attributes import flag_modified

import app.models as models
import app.schema  as schema
import app.schema.worker as work_schema


class CRUDWorkers:
  
    '''
        Workers facade
    '''
    # def get_all(self, db: Session, q: str, skip: int = 0, limit: int = 100) -> List[schema.Worker]:
    #     '''
    #     Get all workers
    #     Parameters:
    #     q - Search by name or surname
    #     '''
    #     items = db.query(models.Worker).filter(models.Worker.name.like(q) | models.Worker.surname.like(q)).offset(skip).limit(limit).all()
    #     return items
    #     #pass

    def get_workers(self, db: Session, skip: int = 0, limit: int = 100) -> List[schema.Worker]:
         items= db.query(models.Worker).offset(skip).limit(limit).all()
         return items

    # def get_all(self, db: Session) -> List[schema.Worker]:
    #     items = db.query(models.Worker).limit(500).all()
    #     return items
   
 
    def get_by_pesel(self, db: Session, pesel: str) -> schema.Worker:
         
         item = db.query(models.Worker).filter(models.Worker.pesel == pesel).first()
         return item
         #pass

    def get_by_name(self, db: Session, name: str) -> List[schema.Worker]:
         
         items = db.query(models.Worker).filter(models.Worker.name == (name)).all()
         return items
         #pass
   
   
 
    def add_worker(self, db: Session, data: models.Worker) -> schema.Worker:
          nw = models.Worker()
          nw.pesel = data.pesel
          nw.name = data.name
          nw.surname = data.surname
          nw.age = data.age
          nw.criminal_record = data.criminal_record
          nw.children = data.children
          nw.department_id = data.department_id
          nw.owner_w = []
        #   nw.salary = 0
          db.add(nw)
          db.commit()
        #   worker = db.query(models.Worker).filter(models.Worker.pesel == data.pesel).one()
          return nw


    # def update_worker(self, db: Session, data: models.Worker) -> schema.Worker:
    #     db.begin()
    #     db.query(models.Worker).filter(models.Worker.pesel == data.pesel).update
    #     (
    #         {"name": data.name},
    #         {"surname": data.surname},
    #         {"age": data.age},
    #         {"criminal_record": data.criminal_record}
    #     )
    #     db.commit()
    #     worker = db.query(models.Worker).filter(models.Worker.pesel == data.pesel).one()
    #     return worker
    
    def update_worker(self, db: Session, data: work_schema.WorkerSimple) -> schema.Worker:
        item = db.query(models.Worker).filter(models.Worker.pesel == data.pesel).one()
        item.name = data.name
        item.surname = data.surname
        item.age = data.age
        # item.criminal_record = data.criminal_record
        db.commit()
        worker = db.query(models.Worker).filter(models.Worker.pesel == data.pesel).one()
        return worker


    def delete(self, db: Session, worker_pesel: str) -> bool:
        worker = db.query(models.Worker).get(worker_pesel)

        if worker:
            # db.begin()
            db.delete(worker)
            db.commit()
        return True
   
    
    def add_or_update_child(self, db: Session, worker_pesel: str, child_schema: schema.Child) -> schema.Worker:

        w_pesel = str(worker_pesel)

        worker = db.query(
            models.Worker
        ) \
        .filter(models.Worker.pesel == w_pesel) \
        .first()

        childs = worker.children

        for child in childs:

            if child["dob"] == child_schema.dob or child["fname"] == child_schema.fname:
                child["imie"] = child_schema.imie
                child["dob"] = child_schema.dob

                flag_modified(worker, "children")

                db.commit()

                return schema.Worker.from_orm(worker)

        json = {'fname' : child_schema.fname,
                 'dob' : child_schema.dob}

        childs.append(json)

        worker.children = childs

        flag_modified(worker, "children")

        db.commit()

        return schema.Worker.from_orm(worker)



    

         # Działa, ale nie sprawdza, czy w jsonie jest już taki wpis - tylko dopisuje dziecko
    # działa tylko wtedy, gdy atrybut dob jest stringiem - trzeba jakoś sparsować datetime, by można było wrzucić do jsona, inaczej wywala błąd
    #wywali bląd, jeśli pole children jest nullem - do poprawki

    #metoda wyciąga listę dzieci z workera, dopisuje nowy element do listy i podmienia ją w bazie 
    def add_child(self, db: Session, worker_pesel: str, child: schema.Child) -> models.Worker:
        item = db.query(models.Worker).filter(
            models.Worker.pesel == worker_pesel).first()
        children = item.children
        json_c = {'dob': child.dob, 'fname': child.fname}
        json.dumps(json_c, default=str)
        try:
            children.append(json_c)
        except AttributeError as e:
            print(e)
        db.query(models.Worker).filter(models.Worker.pesel == worker_pesel).update(
            {"children": children}
        )
        db.commit()

    def get_children(self, db: Session, worker_pesel: str) -> List[schema.Child]:
        items = db.query(models.Worker.children).filter(
            models.Worker.pesel == worker_pesel).all()
        return items


    #Ok
    def add_salary(self, db: Session, worker_pesel: str, month: int, amount: int) -> schema.Worker:
        new_salary = models.Salary(worker_pesel=worker_pesel, month=month, amount=amount)
        db.add(new_salary)
        db.commit()
        worker = db.query(models.Worker).filter(models.Worker.pesel == worker_pesel).one()
        return worker


    #Ok
    def update_salary(self, db: Session, worker_pesel: str, month: int, amount: int) -> schema.Worker:
        db.query(models.Salary).filter(models.Salary.worker_pesel == worker_pesel, models.Salary.month == month).update(
            {"amount": amount})
        db.commit()

