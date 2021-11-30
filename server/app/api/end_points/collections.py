from typing import Optional
from sqlalchemy.orm import Session

from fastapi import Depends, APIRouter, Body
from fastapi.responses import JSONResponse

from app import crud
from app.api import deps
from app.config import settings

from app.schemas.collections import Collection, EditCollection 

import random, string

router = APIRouter()



@router.post("/create")
def insert(
   collection: EditCollection,
   db: Session = Depends(deps.get_db)
):
   db_collection = None

   try:
      db_collection = crud.collection.create(db, collection)

   except Exception as e:
       print(e) 

   if db_collection is None:
      return JSONResponse(status_code=400, content={"message": "Unable to create a new Collection"})

   return JSONResponse(status_code=200, content={"message": "Created successfully"})


@router.get('/{id}', response_model=Collection)
def get_collection(
   id: int,
   db: Session = Depends(deps.get_db)
):
   db_collection = None

   try:
      db_collection = crud.collection.get(db, id)
   except Exception as e:
      print(e)
   
   if db_collection is None:
      return JSONResponse(status_code=400, content={"message": "Unable to fetch collection"})

   return db_collection


@router.patch('/{id}', response_model=Collection)
def update_collection(
   id: int,
   collection: EditCollection,
   db: Session = Depends(deps.get_db)
):
   db_collection = None

   try:
      db_collection = crud.collection.update(db, id, collection)
   except Exception as e:
      print(e)
   
   if db_collection is None:
      return JSONResponse(status_code=400, content={"message": "Unable to update collection"})

   return db_collection

@router.delete('/{id}')
def delete_collection(
   id: int,
   db: Session = Depends(deps.get_db)
):
   isDeleted = False

   try:
      isDeleted = crud.collection.delete(db, id)
   except Exception as e:
      print(e)
   
   if isDeleted:
      return JSONResponse(status_code=200, content={"message": "Deleted successsfully"})

   return JSONResponse(status_code=400, content={"message": "Unable to delete collection"})