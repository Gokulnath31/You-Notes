from sqlalchemy.orm import Session

from fastapi.encoders import jsonable_encoder

from app.models.collections import Collections
from app.models.notes import Notes
from app.schemas.collections import EditCollection



class CRUDCollections:
    def create(self, db: Session, collection: EditCollection):
        collection_dict = collection.dict()
        db_collection = Collections(**collection_dict)
        
        db.add(db_collection)
        db.commit()
        db.refresh(db_collection)
        return db_collection
    
    def get(self, db: Session, id: int):
        return db.query(Collections).filter(Collections.id == id).first()
    
    def update(self, db: Session, id:int, collection: EditCollection):
        db_collection = None
        if (id):
            db_collection = db.query(Collections).filter(Collections.id == id).first()
        else:
            return False
        if db_collection is None:
            return False

        db_collection.name = collection.name if collection.name is not None else db_collection.name

        db.commit()
        db.refresh(db_collection)
        return db_collection
    
    def delete(self, db: Session, id: int):
        affected_rows = 0
        if (id):
            db.query(Notes).filter(Notes.collection_id == id).delete()
            affected_rows = db.query(Collections).filter(Collections.id == id).delete()
        else:
            return False
        if affected_rows <= 0:
            return False
        db.commit()
        return True

collection = CRUDCollections()