from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.authentication.authentication_routes import authentication_router
from app.core.database import init_database, close_database_connect

api_version = "v1"

# using a context manager to create a lifespan
@asynccontextmanager
async def app_lifespan(app: FastAPI):
    try:
        await init_database()
        yield
        print("Server stopped")
    finally:
        # we will close the database connection here
        print("Database connection lost")
        await close_database_connect()



app = FastAPI(
    title = "Ai Powered document analyzer",
    version = api_version,
    lifespan = app_lifespan
)

app.include_router(
    router = authentication_router,
    tags = ["Authentication"],
    prefix = "/api/authentication"
)
