from sqlalchemy.orm import Session

from typing import List, Dict, Any, Optional

import app.models as models
import app.schema  as schema


class CRUDSalary:
  '''
        Salary facade
    '''
  def get_all_by_pesel(self, db: Session, q: str) -> List[schema.Salary]:
        '''
        Get all salaries
 
        Parameters:
        q - Search pesel
        '''
        items = db.query(models.Salary).filter(models.Salary.worker_pesel.like(q)).all()
        return items

  
  def add(self, db: Session, data: models.Salary) -> schema.Salary:
      new_sal = models.Salary()
      new_sal.worker_pesel = data.worker_pesel
      new_sal.month = data.month
      new_sal.amount = data.amount
      db.add(new_sal)
      db.commit()
      return new_sal


  
  def update(self, db: Session, data: models.Salary) -> schema.Salary:
        db.query(models.Salary).filter(models.Salary.id == data.id).update
        (
            {"worker_pesel": data.worker_pesel},
            {"month": data.month},
            {"amount": data.amount},
        )
        db.commit()    



