from fastapi import APIRouter

from app.api.end_points import users, notes, collections

api_router = APIRouter()


api_router.include_router(
    users.router,
    prefix="/users", tags=["Users"])

api_router.include_router(
    notes.router,
    prefix="/notes", tags=["Notes"])

api_router.include_router(
    collections.router,
    prefix="/collections", tags=["Collections"])