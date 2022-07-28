# from sqlalchemy import create_engine, MetaData
# from sqlalchemy.ext.declarative import declarative_base

# engine = create_engine('postgresql+psycopg2://postgres:hola12spg@localhost:5432/trainingdb1105', echo=False)
# Base = declarative_base()
# Meta = MetaData(engine)

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:hola12spg@172.29.77.249:5432/trainingdb1105"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL 
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()