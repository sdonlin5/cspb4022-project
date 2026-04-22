import os
from dotenv import load_dotenv
from sqlalchemy import Engine
from sqlmodel import SQLModel, create_engine




def connect() -> Engine: 
    # creates database engine
    load_dotenv()
    DATABASE_URL = os.getenv('DATABASE_URL')

    if not DATABASE_URL: 
        raise ValueError('DATABASE_URL environment variable not set.')
    engine =  create_engine(DATABASE_URL, echo = True)
    return engine

def create_tables(engine) -> None:
    # creates the database tables
    SQLModel.metadata.create_all(engine)

def drop_all(engine) -> None: 
    # drops all tables from database
    SQLModel.metadata.drop_all(engine)



