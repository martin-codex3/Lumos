from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
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

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail, "errors": []},
    )

# we will customise the errors here 
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    all_errors = [ # type: ignore
        {
            "field": " -> ".join(str(loc) for loc in error["loc"]),
            "message": error["msg"],
            "type": error["type"],
        }
        for error in exc.errors()
    ]

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({
            "message": "Validation failed",
            "errors": all_errors,
        }),
    )
        

app.include_router(
    router = authentication_router,
    tags = ["Authentication"],
    prefix = "/api/authentication"
)
