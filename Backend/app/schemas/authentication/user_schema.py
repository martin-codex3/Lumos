from pydantic import Field, BaseModel, EmailStr
from typing import Annotated
from app.utils.password_policy import validate_password

class UserCreateSchema(BaseModel):

    first_name: str = Field(min_length=5, max_length=50)
    last_name: str = Field(min_length=5, max_length=50)
    email: EmailStr 
    isComplete: bool = Field(default=False)
    password: Annotated[str, validate_password]
