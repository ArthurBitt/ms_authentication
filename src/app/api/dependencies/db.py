#third party
from sqlalchemy.orm import Session

#local
from src.infrastructure.db.base import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()