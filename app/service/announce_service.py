from sqlalchemy.orm import Session
from app.db.crud.announcement_crud import (announce_delete, announce_create, announce_update,
                                           announce_get, announce_search)


def announce_create_service(db: Session, title: str, description: str, author: str):
    announcement = announce_create(db, title, description, author)
    return announcement


def announce_delete_service(db: Session, title: str):
    announce_delete(db, title)


def announce_update_service(db: Session, title: str, description: str, author: str):
    announce = announce_update(db, title, description, author)
    return announce


def announce_find_service(db: Session, title: str):
    announcement = announce_get(db, title)
    return announcement


def announce_search_service(db: Session, title: str, content: str, author: str,  page: int, size: int):
    announcements = announce_search(db, title, content, author, page, size)
    return announcements
