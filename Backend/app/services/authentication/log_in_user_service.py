from app.schemas.authentication.sign_in_schema import SignInSchema
from sqlmodel.ext.asyncio.session import AsyncSession
from app.services.authentication.user_account_service import UserAccountService
from pydantic import EmailStr
from app.utils.password_hasher import verify_hashed_password
from app.utils.jwt_token import create_jwt_token
from datetime import timedelta
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi import status

user_account_service = UserAccountService()

class LoginUserService:

    async def login_in_user(self, session: AsyncSession, user_data: SignInSchema):
        # we have to get the user by the email first
        email: EmailStr = user_data.email
        user_password: str = user_data.password

        user = await user_account_service.get_user_by_email(
            email = email,
            session = session
        )

        if user is not None:
            # we will attempt to get the user password
            verified_password = verify_hashed_password(
                user_password = user_password,
                hashed_password = user.password
            )
            
            if verified_password:
                # we will create the access and refresh tokens here 
                access_token = create_jwt_token(
                    user_data = {
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "email": user.email
                    },
                    refresh = False,
                )

                # for the refresh toke here
                refresh_token = create_jwt_token(
                    user_data = {
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "email": user.email
                    },
                    exp = timedelta(days=7),
                    refresh = True,
                )

                return JSONResponse(
                    content = {
                        "access_token": access_token,
                        "refresh_token": refresh_token
                    }
                )
        raise HTTPException(
            status_code = status.HTTP_403_FORBIDDEN,
            detail = "Email or password is incorrect!"
        )
        

            
        
           

