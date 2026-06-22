from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio.engine import create_async_engine
from sqlalchemy.ext.asyncio.session import async_sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession
from app.core.config import Config
from sqlmodel import SQLModel


# we will create the database engine here 
database_engine: AsyncEngine = create_async_engine(
    url = Config.DATABASE_URL,
    echo = True
)

# this function will attempt to connect to the database here
# we will use this to create a database session later 
async def init_database():
    async with database_engine.begin() as connection:
        await connection.run_sync(SQLModel.metadata.create_all)

async def close_database_connect():
    await database_engine.dispose()

# we will create the database session here 
# this will be used for the dependency injection
database_session = async_sessionmaker(
    bind=database_engine,
    class_=AsyncSession,
    expire_on_commit = False
)

async def get_database_session():
    async with database_session() as session:
        yield session
