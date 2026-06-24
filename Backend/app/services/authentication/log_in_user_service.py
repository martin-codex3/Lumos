from schemas.authentication.sign_in_schema import SignInSchema
from sqlmodel.ext.asyncio.session import AsyncSession
from services.authentication.user_account_service import UserAccountService
from pydantic import EmailStr
from utils.password_hasher import verify_hashed_password


user_account_service = UserAccountService()

class LoginUserService:

    def __init__(self, session: AsyncSession, user_data: SignInSchema) -> None:
        self.session = session
        self.user_data = user_data

    async def login_in_user(self):
        # we have to get the user by the email first
        email: EmailStr = self.user_data.email
        user_password: str = self.user_data.password

        user = await user_account_service.get_user_by_email(
            email = email,
            session = self.session
        )

        if user is not None:
            # we will attempt to get the user password
            verified_password = verify_hashed_password(
                user_password = user_password,
                hashed_password = user["password"]
            )
            print(verified_password)