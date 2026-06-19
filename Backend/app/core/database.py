from sqlmodel import create_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from app.core.config import Config
from sqlmodel import SQLModel

# we will create the database engine here 
database_engine = AsyncEngine(
    create_engine(
        url = Config.DATABASE_URL,
        echo = True
    )
)

# this function will attempt to connect to the database here
# we will use this to create a database session later 
async def init_database():
    async with database_engine.begin() as connection:
        await connection.run_sync(SQLModel.metadata.create_all)

async def close_database_connect():
    async with database_engine.begin() as connection:
        connection.close
