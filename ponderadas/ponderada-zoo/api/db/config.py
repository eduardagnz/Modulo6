from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite3://database.db")

session = Session(engine)

Base = declarative_base()