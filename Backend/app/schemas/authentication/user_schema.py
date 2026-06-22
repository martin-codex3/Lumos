from pydantic import Field, BaseModel, EmailStr


class USerCreateSchema(BaseModel):

    first_name: str = Field(min_length=5, max_length=50)
    last_name: str = Field(min_length=5, max_length=50)
    email: EmailStr 
    isComplete: bool = Field(default=False)
    password: str = Field(min_length=5, max_length=20)
