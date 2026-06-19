from fastapi import FastAPI
from app.api.authentication_routes import authentication_router


api_version = "v1"

app = FastAPI(
    title = "Ai Powered document analyzer",
    version = api_version
)

app.include_router(
    router = authentication_router,
    tags = ["Authentication"],
    prefix = "/api/authentication"
)
