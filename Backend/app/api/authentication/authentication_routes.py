from fastapi import APIRouter, status, Depends
from app.services.authentication.user_account_service import UserAccountService
from app.schemas.authentication.user_schema import USerCreateSchema
from sqlmodel.ext.asyncio.session import AsyncSession
from app.mappings.authentication.create_user_response import CreateUserResponse
from pydantic import EmailStr

authentication_router = APIRouter()
# we will get the services here 
authentication_services = UserAccountService()

@authentication_router.get("/create-account", status_code = status.HTTP_200_OK, response_model = CreateUserResponse)
async def index(user_data: USerCreateSchema, session: AsyncSession):
    # we have to check if the user exists 
    email: EmailStr = user_data.email

    user_exists = await authentication_services.check_if_user_exists(
        email = email,
        session = session
    )

    if user_exists:
        return 