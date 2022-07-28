from imp import reload
import json
from unicodedata import name
from xmlrpc.client import Boolean
from fastapi import Depends, FastAPI, HTTPException, Request, Form
from fastapi import APIRouter
from sqlalchemy.orm import sessionmaker, Session
import uvicorn
from connection import SessionLocal, engine
import app.models as models
import app.schema as schema
import app.schema.worker as work_schema
from app.crud import CRUDDepartment
from app.crud import CRUDWorkers
from app.crud import CRUDSalary
# from fastapi.templating import Jinja2Templates
# from starlette.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware


from connection import Base



Base.metadata.create_all(bind=engine)

app = FastAPI()
api = APIRouter()

origins = [
    "http://localhost",
    "http://127.0.0.1:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# app.mount("/static", StaticFiles(directory="static"), name="static")


# templates = Jinja2Templates(directory="templates")

@api.get("/")
async def index():
    return dict(message= "Hello from FastAPI")



df = CRUDDepartment()

@api.get("/departments/department/{q}", response_model=schema.Department)
async def read_department(q: int, db: Session  = Depends(get_db)):
    department = df.get(db, q)
    return department

# @api.get("/departments/", response_model = list[schema.Department])
# def read_departments(skip: int= 0, limit: int = 100, db:Session = Depends(get_db)):
#     items = df.get_departments(db, skip=skip, limit=limit)
#     return items

@api.get("/departments/all/{name}", response_model=list[schema.Department])
def read_all_departments(name: str, skip: int= 0, limit: int = 100, db:Session  = Depends(get_db)):
    print(name)
    
    items = df.get_all(db, q=name, skip=skip, limit=limit)
    return items

# Editing departments.

@api.put("/departments/edit", response_model= schema.DepartmentBase) 
def dep_edit(department: schema.DepartmentBase, db:Session= Depends(get_db)):
    return df.update_department(db=db,data = department)
 
@api.post("/departments/worker/add/{department_id}/{worker_pesel}", response_model = schema.Department)
def create_worker( department_id: int, worker_pesel: str, db:Session  = Depends(get_db)):
    print ('create_worker')
    # db_department = df.get(db, id = data.id)
    # if db_department:
    #     raise HTTPException(status_code=400, detail="Department already exist")
    return df.add_worker(db=db,department_id= department_id, worker_pesel=worker_pesel)

@api.delete("/departments/{department_id}", response_model = bool)
def delete_department( department_id: int, db:Session  = Depends(get_db)):
    return df.delete(db=db, department_id=department_id)

@api.put("/departments/department/{department_id}/{worker_pesel}", response_model= bool) 
def delete_worker(department_id : int, worker_pesel: str, db:Session= Depends(get_db)):
    return df.delete_worker(db=db,department_id = department_id, worker_pesel=worker_pesel)

# metoda na pobranie z formularza
@api.post("/departments/add", response_model=schema.Department)
async def create_department(department : schema.DepartmentCreate, db: Session = Depends(get_db)):

    # print ('create_department')
    # dep_form = await r.form()
    # department = schema.Department(**dep_form)
    # new_department = df.add_department(db=db, data=department)
    # return new_department
    return df.create_department(db=db, data = department)



wf = CRUDWorkers()

@api.get("/workers/all/{name}", response_model=list[schema.Worker])
def read_workers( skip: int = 0, limit: int=100, db: Session  = Depends(get_db)):
    workers = wf.get_workers(db,  skip=skip, limit=limit)
    return workers

# @api.get('/workers/all', response_model=list[schema.Worker])
# def get_all_workers(db: Session = Depends(get_db)):
#  users = wf.get_all(db=db)
#  return users

@api.get('/workers/worker/{pesel}', response_model=schema.Worker)
def get_worker_by_pesel(pesel: str, db: Session = Depends(get_db)):
  worker = wf.get_by_pesel(db=db, pesel=pesel)
  return worker

@api.get('/workers/{name}', response_model=list[schema.Worker])
def get_worker_by_name(name: str, db:Session = Depends(get_db)):
    worker = wf.get_by_name(db=db, name=name )
    return worker


@api.post("/workers/add", response_model=schema.Worker)
def create_new_worker(data:schema.Worker ,db:Session = Depends(get_db)):
    return wf.add_worker(db=db, data=data)

####Już działa
@api.put("/workers/update", response_model=schema.Worker)
def update_worker(data: work_schema.WorkerSimple, db:Session = Depends(get_db)):
    return wf.update_worker(db=db, data=data)

@api.delete("/workers/delete/{worker_pesel}", response_model = bool)
def delete_worker( worker_pesel: str, db:Session  = Depends(get_db)):
    print('jestesmy tu')
    return wf.delete(db=db, worker_pesel=worker_pesel)

@api.get('/users/children/id/{worker_pesel}')
def get_children(worker_pesel: str, db: Session = Depends(get_db)):
    children = wf.get_children(db=db, worker_pesel=worker_pesel)
    return children



'''Join with HTML form'''


# @api.get('/html')
# async def html():

#     file= f'C:\\Users\\sshvets\\Desktop\\projects\\sql_alchemy_tutor\\app\\templates\\index.html'

#     if file:
#         return FileResponse(file)

#     # if os.path.exists(file):
#     #     return templates.TemplateResponse('formularz.html', {'request': request})
#     # else:
#     #     return HTTPException(404, 'Not found')

@api.post('/html_submit')
async def login(user: str = Form(...), password: str = Form(...), department: str = Form(...)):

    return {'username':user, 'password': bool(password), 'department': department}





# if __name__ == '__main__':    
    # SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    # session = SessionLocal()
    # uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info", reload=True)


    # df = CRUDDepartment()
    # wf = CRUDWorkers()
    # sf = CRUDSalary()

# @api.middleware("http")
# async def db_session_middleware(request: Request, call_next):
#     response = Response("Internal server error", status_code=500)
#     try:
#         request.state.db = SessionLocal()
#         response = await call_next(request)
#     finally:
#         request.state.db.close()
#     return response
# Dependency

# @api.get("/users/", response_model=list[schema.Department])
# def read_users(skip: int = 0, limit: int = 100, db: Session  = Depends(get_db)):
#     users = df.get_users(db, skip=skip, limit=limit)
#     return users

# @api.post("/users/", response_model=schema.Department)
# def create_user(user: schema.Department, db: Session = Depends(get_db)):
#     db_user = df.get_user_by_id(db, id=user.id)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return df.add(db=db, user=user)

    #with SessionLocal() as db:

        #####adding new worker
        # salary_list = []

        # dep_for_worker = df.get(db=db, department_id=17)


        # new_worker = schema.Worker(pesel='12345678901', name='Sofiia', surname='Shvets', age=22, criminal_record=False, salary=salary_list, department=dep_for_worker)
        # print(new_worker)
        # wf.add_worker(db=db, data=new_worker)
        #   '''
        #      Creating and adding new Child object
        #     '''
        # child_of_nw = schema.Child(fname='Lucy', dob='2019-12-04')


        # wf.add_child(db=db, worker_pesel='000007352016', child=child_of_nw)
          ###############################UPDATE_CHILD ERROR##################################################  
        # my_json = [{'dob': '2018-06-22T14:06:12.358997', 'fname': 'Kuba'}]  
        # #chlid_schema = schema.Child(fname='Kamil',dob = '1997-06-01T22:33:02.021817')

        # wf.add_or_update_child(session,18163388594 ,my_json)


        # worker = wf.get(session,18163326656) 


        # c = schema.Child(dob='2015-01-23T09:11:47.134195', fname='AAAAAAAAAA')
        # # crudwork.add_child(db=db, worker_pesel='11', child=c)
        # wf.add_child(db=db, worker_pesel='86978456300', child=c)

        
        # child_for_update = schema.Child(fname='Lily', dob='2021-19-03')

        # item = wf.update_child(db=db, worker_pesel='000007352016', child=child_for_update)
        # print(item)
        




        ###update is correct
        # new_dep = schema.Department(id=197, name='Dcline', street='Jagiellońska 42', city='Radomyśl', postcode='23-455', workers_no=99)
        #df.update(db = db, data= new_dep)


        ###add is correct
        ###df.add(db=db, data=new_dep)
        
        ###workers operation in department table
        #df.add_worker(db=db, department_id=7342, worker_pesel='20099912332')
        #df.delete_worker(db=db, department_id=7342, worker_pesel='20099912332')
        

        # item = sf.get_all_by_pesel(db, '00201799220')
        # print(item)

        # new_salary = schema.Salary(id=44, worker_pesel='00213286793', month=9, amount=700000)
        # item =sf.update(db=db, data=new_salary)
        # print(item)

        # item = wf.get_by_name(db, 'Gregori')
        # print (item)
        
        # items = df.get_all(db, 'Samsung Electronics')
        # print (len(items))

        # items = df.get_all(db, 'ENEA')
        # print(len(items))

        # count = df.count(db, 'Samsung Electronics')
        # print (count)

app.include_router(api, prefix='/api/v1')