from pydantic import BaseModel, EmailStr, AfterValidator
from typing import Annotated
from app.utils.password_policy import validate_password

class SignInSchema(BaseModel):

    email: EmailStr 
    password: Annotated[str, AfterValidator(validate_password)]
