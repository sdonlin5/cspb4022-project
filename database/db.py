import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from sqlmodel import SQLModel

import models.play
import models.situation
import models.schedule

load_dotenv()

def get_db_url() -> str:
    url = os.getenv('DATABASE_URL')
    if not url:
        raise ValueError('DATABASE_URL environment variable not set.')
    return url

# --- 1. SYNC ENGINE (For Streamlit/Reads) ---
sync_url = get_db_url().replace("+asyncpg", "")
sync_engine = create_engine(sync_url, pool_pre_ping=True)

# --- 2. ASYNC ENGINE (For Pipeline/Writes) ---
async_engine: AsyncEngine = create_async_engine(get_db_url(), future=True)

async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

async def drop_all():
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)