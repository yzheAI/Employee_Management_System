from sqlalchemy.orm import Session

from app.core.exceptions import PermissionDenied
from app.db.crud.announcement_crud import (announce_delete, announce_create, announce_update,
                                           announce_get, announce_search)


def announce_create_service(db: Session, title: str, description: str, author: str, user: dict):
    if user["role"] != "admin":
        raise PermissionDenied("管理员才能创建公告")
    announcement = announce_create(db, title, description, author)
    return announcement


def announce_delete_service(db: Session, title: str, user: dict):
    if user["role"] != "admin":
        raise PermissionDenied("管理员才能删除公告")
    announce_delete(db, title)


def announce_update_service(db: Session, title: str, description: str, author: str, user: dict):
    if user["role"] != "admin":
        raise PermissionDenied("管理员才能修改")
    announce = announce_update(db, title, description, author)
    return announce


def announce_find_service(db: Session, title: str):
    announcement = announce_get(db, title)
    return announcement


def announce_search_service(db: Session, keyword: str, page: int, size: int):
    announcements = announce_search(db, keyword, page, size)
    return announcements
