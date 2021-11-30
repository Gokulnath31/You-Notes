from app.db.base_class import Base

import enum

from sqlalchemy.orm import relationship

from sqlalchemy import Column, ForeignKey, Integer, String, func, JSON, Boolean
from sqlalchemy.dialects.mysql import DATETIME, ENUM

class SOURCE(enum.Enum):
    YOUTUBE = 'YOUTUBE'
    ARTICLES = 'ARTICLES'
    DOCUMENTATION = 'DOCUMENTATION'
    OTHERS = 'OTHERS'


class Notes(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    tags = Column(JSON)
    markdown_text = Column(String(255))
    user_id = Column(Integer, ForeignKey("users.id"))
    collection_id = Column(Integer, ForeignKey("collections.id"))
    source = Column(ENUM(SOURCE), server_default="SOURCE")
    visibility = Column(Boolean, unique=False, default=True)
    created = Column(DATETIME, server_default=func.current_timestamp())
    modified = Column(DATETIME, server_default=func.current_timestamp(),
                      onupdate=func.now())

    user_detail = relationship("Users")
    collection_detail = relationship("Collections")
