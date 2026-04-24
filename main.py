from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database.db import create_tables, get_session

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Action on startup
    await create_tables()
    yield
    # Action on shutdown (if needed)

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root(session: AsyncSession = Depends(get_session)):
    return {"message": "Hello World!"}