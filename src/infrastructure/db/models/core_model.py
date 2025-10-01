# third-party
from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from src.core.utils.date_handler import date_handler
from uuid import uuid4
# local
from src.infrastructure.db.base import Base


class CoreModel(Base):
    __abstract__ = True

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=date_handler.now_utc())
    updated_at = Column(DateTime, default=date_handler.now_utc(), onupdate=date_handler.now_utc())

    def save(self, session):
        session.add(self)
        session.commit()
        session.refresh(self)
        return self
