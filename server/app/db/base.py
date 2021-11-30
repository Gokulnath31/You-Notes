# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  
from app.models.users import Users  
from app.models.notes import Notes  
from app.models.collections import Collections 