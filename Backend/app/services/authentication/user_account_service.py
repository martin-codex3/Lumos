from sqlmodel.ext.asyncio.session import AsyncSession
from app.models.user import User
from sqlmodel import select
from pydantic import EmailStr
from app.schemas.authentication.user_schema import USerCreateSchema

class UserAccountService:
    """we will have all the user account creation here"""

    async def get_user_by_email(self, email: EmailStr, session: AsyncSession) -> object:
        statement = select(User).where(User.email == email)
        results = await session.exec(statement)

        return results.first()
    
    # we will attempt to check if the user exists here 
    async def check_if_user_exists(self, email: EmailStr, session: AsyncSession) -> bool:
        user = await self.get_user_by_email(
            email = email,
            session = session
        )

        if user is not None:
            return True
        else:
            return False
    
    # we will attempt to create the user account here 
    async def create_user_account(self, user_data: USerCreateSchema, session: AsyncSession):
        user_data_dict = user_data.model_dump()

        new_user = User(**user_data_dict)

        session.add(new_user)
        await session.commit()