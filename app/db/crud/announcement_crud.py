from datetime import datetime

from sqlalchemy.orm import Session

from app.core.exceptions import ConflictError, NotFoundError
from app.models.announcement import Announcement
from app.schemas.announce_schema import AnnounceResponse
from utils.pagination import paginate
from utils.query_builder import apply_filters, base_query


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


# must exist
def announce_get(db: Session, title: str):
    announce = announce_find(db, title)
    if not announce:
        raise NotFoundError("not found announcement")
    return announce


def announce_find(db: Session, title: str):
    query = base_query(db, Announcement)
    return query.filter(Announcement.title == title).first()


def announce_delete(db: Session, title) -> bool:
    announce = announce_get(db, title)
    announce.is_deleted = True
    announce.deleted_at = datetime.utcnow()
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


def announce_search(db: Session, title: str, content: str, author: str, page: int, size: int):
    query = base_query(db, Announcement)

    conditions = []

    if title.strip():
        conditions.append(
            Announcement.title.ilike(f"%{title}%")
        )
    if content.strip():
        conditions.append(
            Announcement.content.ilike(f"%{content}%")
        )
    if author.strip():
        conditions.append(
            Announcement.author.ilike(f"%{author}%")
        )

    query = apply_filters(query, conditions)
    result = paginate(query, page, size, AnnounceResponse)
    return result
