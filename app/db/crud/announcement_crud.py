from datetime import datetime

from sqlalchemy.orm import Session

from app.core.response import error
from app.models.announcement import Announcement


def announce_create(db: Session, title: str, content: str, author: str):
    announce_db = announce_find(db, title)
    if announce_db:
        return error(400, "标题已存在")
    announcement = Announcement(
        title=title,
        content=content,
        author=author,
        date=datetime.utcnow()
    )
    db.add(announcement)
    db.commit()
    db.refresh(announcement)
    return announcement


def announce_find(db: Session, title: str):
    announce = db.query(Announcement).filter(Announcement.title == title).first()
    return announce


def announce_show_all(db: Session):
    announces = db.query(Announcement).all()
    return announces


def announce_delete(db: Session, title) -> bool:
    announce = announce_find(db, title)
    if not announce:
        return False
    db.delete(announce)
    db.commit()
    return True
