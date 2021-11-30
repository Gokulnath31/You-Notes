from typing import Optional
from sqlalchemy.orm import Session

from fastapi import Depends, APIRouter, Body
from fastapi.responses import JSONResponse

from app import crud
from app.api import deps
from app.config import settings

from app.schemas.users import CreateUser, UserLogin

import random, string


router = APIRouter()


@router.post("/signup")
def insert(
   user: CreateUser,
   db: Session = Depends(deps.get_db)
):

   new_user = None
   try:
      new_user = crud.user.create(db,user)
   
   except Exception as e:
      print(e)
   if new_user is None:
      return JSONResponse(status_code=400, content={"message": "Unable to create a new user"})
   return JSONResponse(status_code=200, content={"message": "Created successfully"})


@router.post("/login")
def login(
   user_credentials: UserLogin, 
   db: Session = Depends(deps.get_db)
):

   user = None
   try:
      user = crud.user.get_user(db,user_credentials)

      if user.password != user_credentials.password:
         raise Exception("Invalid email or password")

      return JSONResponse(status_code=200, content={"message": "Login Success"})
   except Exception as e:
      return JSONResponse(status_code=400, content={"message": "Invalid email or password"})

