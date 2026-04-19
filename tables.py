from sqlmodel import SQLModel
 

from .db.engine import start

def create():
    SQLModel.metadata.create_all(start)

def delete(): 
    print("Confirm all tables will be deleted: yes or no")
    confirm = input()
    
    if confirm == "yes": 
        SQLModel.metadata.drop_all()
    else: 
        exit