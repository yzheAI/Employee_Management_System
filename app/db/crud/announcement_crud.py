from datetime import datetime

from sqlalchemy.orm import Session

from app.core.exceptions import ConflictError, NotFoundError
from app.models.announcement import Announcement


def announce_create(db: Session, title: str, content: str, author: str):
    announce_db = announce_find(db, title)
    if announce_db:
        raise ConflictError("标题已存在")
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


def announce_get(db: Session, title: str):
    announce = db.query(Announcement).filter(Announcement.title == title).first()
    if not announce:
        raise NotFoundError("not found announcement")
    return announce


def announce_find(db: Session, title: str):
    return db.query(Announcement).filter(Announcement.title == title).first()


def announce_show_all(db: Session):
    announces = db.query(Announcement).all()
    return announces


def announce_delete(db: Session, title) -> bool:
    announce = announce_get(db, title)
    db.delete(announce)
    db.commit()
    return True
