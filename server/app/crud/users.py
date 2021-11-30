from sqlalchemy.orm import Session

from fastapi.encoders import jsonable_encoder

from app.models.users import Users
from app.schemas.users import CreateUser, UserLogin


class CRUDUsers:
    def create(self, db: Session, user: CreateUser):
        db_user = Users(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            password=user.password,
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    def get_user(self, db: Session, user:UserLogin):
        return db.query(Users).filter(Users.email == user.email).first()

user = CRUDUsers()