from app.db.base_class import Base

from sqlalchemy import Column, Integer, String, func, JSON
from sqlalchemy.dialects.mysql import DATETIME


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255), unique=True)
    password = Column(String(255))
    created = Column(DATETIME, server_default=func.current_timestamp())
    modified = Column(DATETIME, server_default=func.current_timestamp(),
                      onupdate=func.now())

