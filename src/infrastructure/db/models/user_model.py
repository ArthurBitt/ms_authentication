# third-party
from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from passlib.context import CryptContext
from datetime import datetime

# local
from src.infrastructure.db.models.core_model import CoreModel


class UserModel(CoreModel):
    __tablename__ = "users"

    name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    def set_password(self, raw_password: str):
        self.password = pwd_context.hash(raw_password)

    def verify_password(self, raw_password: str) -> bool:
        return pwd_context.verify(raw_password, self.password)
