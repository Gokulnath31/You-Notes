from typing import Optional
from sqlalchemy.orm import Session

from fastapi import Depends, APIRouter, Body
from fastapi.responses import JSONResponse

from app import crud
from app.api import deps
from app.config import settings

from app.schemas.notes import Note, CreateNote, EditNote

import random, string

router = APIRouter()


@router.post("/create")
def insert(
   note: CreateNote,
   db: Session = Depends(deps.get_db)
):
   db_note = None

   try:
      db_note = crud.note.create(db, note)

   except Exception as e:
       print(e) 

   if db_note is None:
      return JSONResponse(status_code=400, content={"message": "Unable to create a new note"})

   return JSONResponse(status_code=200, content={"message": "Created successfully"})


@router.get('/{id}', response_model=Note)
def get_note(
   id: int,
   db: Session = Depends(deps.get_db)
):
   db_note = None

   try:
      db_note = crud.note.get_note(db, id)
   except Exception as e:
      print(e)
   
   if db_note is None:
      return JSONResponse(status_code=400, content={"message": "Unable to fetch note"})

   return db_note


@router.patch('/{id}', response_model=Note)
def update_note(
   id: int,
   note: EditNote,
   db: Session = Depends(deps.get_db)
):
   db_note = None

   try:
      db_note = crud.note.update_note(db, id, note)
   except Exception as e:
      print(e)
   
   if db_note is None:
      return JSONResponse(status_code=400, content={"message": "Unable to update note"})

   return db_note


@router.delete('/{id}')
def delete_note(
   id: int,
   db: Session = Depends(deps.get_db)
):
   isNoteDeleted = False

   try:
      isNoteDeleted = crud.note.delete_note(db, id)
   except Exception as e:
      print(e)
   
   if isNoteDeleted:
      return JSONResponse(status_code=200, content={"message": "Deleted successsfully"})

   return JSONResponse(status_code=400, content={"message": "Unable to delete note"})

      
   