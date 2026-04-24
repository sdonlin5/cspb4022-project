import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from models.play import Play
from models.situation import Situation
from models.schedule import Schedule

load_dotenv()

def get_async_engine() -> AsyncEngine:
    DATABASE_URL = os.getenv('DATABASE_URL')
    if not DATABASE_URL:
        raise ValueError('DATABASE_URL environment variable not set.')
    return create_async_engine(DATABASE_URL, echo=True, future=True)

# Global engine instance
engine = get_async_engine()

async def create_tables() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

async def drop_all() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)

async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session