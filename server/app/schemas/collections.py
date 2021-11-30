from datetime import date, datetime, time, timedelta

from pydantic import BaseModel
from typing import Optional

from app.models import SOURCE


class Collection(BaseModel):
    id: int
    name: Optional[str]
    created :datetime
    modified:datetime

    class Config:
        orm_mode = True

class EditCollection(BaseModel):
    name: Optional[str]

    class Config:
        orm_mode = True
