from pydantic import EmailStr, BaseModel
from datetime import datetime

class CreateUserResponse(BaseModel):

    first_name: str
    last_name: str
    email: EmailStr
    isComplete: bool
    created_at: datetime
    updated_at: datetime