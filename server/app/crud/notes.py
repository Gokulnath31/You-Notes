from sqlalchemy.orm import Session

from fastapi.encoders import jsonable_encoder

from app.models.notes import Notes, SOURCE
from app.schemas.notes import CreateNote, EditNote


class CRUDNotes:
    def create(self, db: Session, note: CreateNote):
        note_dict = note.dict()
        db_note = Notes(**note_dict)
        
        db.add(db_note)
        db.commit()
        db.refresh(db_note)
        return db_note
    
    def get_note(self, db: Session, id: int):
        return db.query(Notes).filter(Notes.id == id).first()
    
    def update_note(self, db: Session, id:int, note: EditNote):
        db_note = None
        if (id):
            db_note = db.query(Notes).filter(Notes.id == id).first()
        else:
            return False
        if db_note is None:
            return False

        db_note.title = note.title if note.title is not None else db_note.title
        db_note.source =  note.source if note.source is not None else db_note.source
        db_note.visibility =  note.visibility if note.visibility is not None else db_note.visibility
        db_note.markdown_text =  note.markdown_text if note.markdown_text is not None else db_note.markdown_text
        db_note.tags =  note.tags if note.tags is not None else db_note.tags

        db.commit()
        db.refresh(db_note)
        return db_note
    
    def delete_note(self, db: Session, id: int):
        affected_rows = 0
        if (id):
            affected_rows = db.query(Notes).filter(Notes.id == id).delete()
        else:
            return False
        if affected_rows <= 0:
            return False
        db.commit()
        return True


note = CRUDNotes()