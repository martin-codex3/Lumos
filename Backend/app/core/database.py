from sqlmodel import create_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from app.core.config import Config

# we will create the database engine here 
database_engine = AsyncEngine(
    create_engine(
        url = Config.DATABASE_URL,
        echo = True
    )
)

# this function will attempt to connect to the database here
# we will use this to create a database session later 
