from sqlmodel import SQLModel, Field, Column
from datetime import datetime
import sqlalchemy.dialects.postgresql as pg
import uuid

class User(SQLModel, table=True):
    __tablename__ = "users" # type: ignore

    user_id: uuid.UUID = Field(
        sa_column=Column(pg.UUID, primary_key=True, nullable=False, unique=True, default=uuid.uuid4)
    )
    first_name: str = Field(index=True, nullable=False)
    last_name: str = Field(index=True, nullable=False)
    email: str = Field(index=True, unique=True)
    is_complete: bool = Field(default=False, index=True)
    password: str = Field(nullable=False)
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))