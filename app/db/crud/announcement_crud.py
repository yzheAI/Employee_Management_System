from datetime import datetime

from sqlalchemy.orm import Session

from app.core.exceptions import ConflictError, NotFoundError
from app.models.announcement import Announcement
from app.schemas.announce_schema import AnnounceResponse


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


def announce_show_all(db: Session, page: int, size: int):
    total = db.query(Announcement).count()
    skip = (page - 1) * size
    announces = db.query(Announcement).offset(skip).limit(size).all()
    re_announcement = {
        "page": page,
        "size": size,
        "total": total,
        "items": [AnnounceResponse.model_validate(i) for i in announces],
    }
    return re_announcement


def announce_delete(db: Session, title) -> bool:
    announce = announce_get(db, title)
    db.delete(announce)
    db.commit()
    return True


def announce_update(db: Session, title: str, content: str, author: str):
    announcement = announce_get(db, title)
    announcement.content = content
    announcement.author = author
    announcement.date = datetime.utcnow()
    db.commit()
    db.refresh(announcement)
    return announcement

