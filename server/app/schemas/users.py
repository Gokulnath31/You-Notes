from datetime import date, datetime, time, timedelta

from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: int
    first_name: str
    last_name: Optional[str]
    email: str
    created: datetime
    modified: datetime

    class Config:
        orm_mode = True

class CreateUser(BaseModel):
    first_name: str
    last_name: Optional[str]
    email: str
    password: str

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True