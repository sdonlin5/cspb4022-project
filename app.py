"""
Main application for the project. 
"""

from fastapi import FastAPI
import db
import models

app = FastAPI()
engine = db.engine()


@app.get("/")
async def root(): 
    return {"message": "Hello World"}
