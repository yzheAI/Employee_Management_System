from app.db.session import Base
from sqlalchemy import Column, String


class Announcement(Base):
    __tablename__ = 'announcement'
    title = Column(String(128), primary_key=True, index=True)
    content = Column(String(4096))
    author = Column(String(64))
    date = Column(String(64))
