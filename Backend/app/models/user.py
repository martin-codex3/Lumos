from sqlmodel import SQLModel, Field, Column
from datetime import datetime
import sqlalchemy.dialects.postgresql as pg


class User(SQLModel, table = True):

    __tablename__ "users"

    firstName: str = Field(index = True, nullable = False)
    lastName: str = Field(index = True, nullable = False)
    email: str = Field(index = True, unique = True)
    isComplete: bool = Field(default = False, index = True)
    password: str = Field(nullable = False)
    createdAt: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updatedAt: datetime = Field(sa_column=Column(pg.TIMESTAMP, default = datetime.now))
    
