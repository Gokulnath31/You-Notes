from typing import Generator
from fastapi import Depends, HTTPException, status

from app.config import settings
from app.db.session import SessionLocal


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()