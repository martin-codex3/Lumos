from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.authentication_routes import authentication_router
from app.core.database import init_database

api_version = "v1"

# using a context manager to create a lifespan
@asynccontextmanager
async def app_lifespan():
    try:
        init_database()
    finally:
        # we will close the database connection here
        print("Database connection lost")


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
