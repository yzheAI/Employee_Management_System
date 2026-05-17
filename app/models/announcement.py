from datetime import datetime

from app.db.session import Base
from sqlalchemy import Column, String, DateTime, Boolean


class Announcement(Base):
    __tablename__ = 'announcement'
    title = Column(String(128), primary_key=True, index=True)
    content = Column(String(4096))
    author = Column(String(64))
    date = Column(DateTime, default=datetime.utcnow)
    is_deleted = Column(Boolean, default=False)
    deleted_at = Column(DateTime, nullable=True)
