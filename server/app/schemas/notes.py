from datetime import date, datetime, time, timedelta

from pydantic import BaseModel
from typing import Optional

from app.models import SOURCE


class Note(BaseModel):
    id: int
    title: str
    tags: Optional[list]
    markdown_text: str
    user_id: int
    collection_id: Optional[int]
    source: Optional[SOURCE]
    visibility :bool
    created :datetime
    modified:datetime

    class Config:
        orm_mode = True


class CreateNote(BaseModel):
    user_id: int
    title: str
    tags: Optional[list]
    markdown_text: str
    collection_id: Optional[int]
    source: Optional[SOURCE]
    visibility :bool

    class Config:
        orm_mode = True

class EditNote(BaseModel):
    title: str
    tags: Optional[list]
    markdown_text: str
    source: Optional[SOURCE]
    visibility :bool

    class Config:
        orm_mode = True