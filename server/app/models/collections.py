from app.db.base_class import Base

from sqlalchemy import Column, Integer, String, func
from sqlalchemy.dialects.mysql import DATETIME


class Collections(Base):
    __tablename__ = "collections"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    created = Column(DATETIME, server_default=func.current_timestamp())
    modified = Column(DATETIME, server_default=func.current_timestamp(),
                      onupdate=func.now())