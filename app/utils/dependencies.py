from sqlalchemy.orm import Session
from fastapi import Depends
from app.db.database import get_db
from app.models.user import User

def get_current_user(db: Session = Depends(get_db)):
    return db.query(User).first()  # Placeholder for actual authentication logic