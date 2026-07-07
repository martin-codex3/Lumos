from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.responses import JSONResponse
from app.services.authentication.user_account_service import UserAccountService
from app.schemas.authentication.user_schema import UserCreateSchema
from app.schemas.authentication.sign_in_schema import SignInSchema
from sqlmodel.ext.asyncio.session import AsyncSession
from app.mappings.authentication.create_user_response import CreateUserResponse
from pydantic import EmailStr
from app.core.database import get_database_session
from app.services.authentication.log_in_user_service import LoginUserService
from app.dependencies.dependency import RefreshTokenBearer
from app.utils.jwt_token import create_jwt_token
from datetime import datetime, timedelta

authentication_router = APIRouter()
# we will get the services here 
authentication_services = UserAccountService()
login_user_service = LoginUserService()
refresh_token_bearer = RefreshTokenBearer()

@authentication_router.post("/create-account", status_code = status.HTTP_200_OK, response_model = CreateUserResponse)
async def index(user_data: UserCreateSchema, session: AsyncSession = Depends(get_database_session)):
    # we have to check if the user exists 
    email: EmailStr = user_data.email

    user_exists = await authentication_services.check_if_user_exists(
        email = email,
        session = session
    )

    if user_exists:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "User with that email already exists"
        )
    else:
        # we will create the user here 
        new_user = await authentication_services.create_user_account(
            user_data = user_data,
            session = session
        )
        return new_user


@authentication_router.post("/sign-in", status_code=status.HTTP_200_OK)
async def sign_in(user_data: SignInSchema, session: AsyncSession = Depends(get_database_session)):

    user_login = await login_user_service.login_in_user(
        session = session,
        user_data = user_data
    )

    return user_login



# we will attempt to create the refresh tokens here 
@authentication_router.get("/refresh", status_code = status.HTTP_200_OK)
async def create_refresh_token(token_details: dict = Depends(refresh_token_bearer)):
    token_expiry_timestamp = token_details["exp"]

    if datetime.fromtimestamp(token_expiry_timestamp) > datetime.now():
        new_access_token = create_jwt_token(user_data = token_details["user"])

        return JSONResponse(
            content = {"access_token": new_access_token}
        )

