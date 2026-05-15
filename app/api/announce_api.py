from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.response import error, success
from app.core.security import get_current_user
from app.db.session import get_db
from app.schemas.response_schema import ResponseModel
from app.schemas.announce_schema import AnnounceResponse, AnnounceCreate
from app.db.crud.announcement_crud import announce_create, announce_delete, announce_get, announce_show_all, \
    announce_update

announce_router = APIRouter(prefix="/announcement", tags=["公告"])


@announce_router.post("/", response_model=ResponseModel[AnnounceResponse], summary="添加公告")
def create_announce(announce: AnnounceCreate, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    if user["role"] != "admin":
        return error(403, "只有管理员能添加")
    a = announce_create(db, announce.title, announce.content, announce.author)
    return success(AnnounceResponse.model_validate(a))


@announce_router.get("/{title}", response_model=ResponseModel[AnnounceResponse], summary="查找公告")
def get_announce(title: str, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    announce_db = announce_get(db, title)
    return success(AnnounceResponse.model_validate(announce_db))


@announce_router.get("/", response_model=ResponseModel[list[AnnounceResponse]], summary="获取所有公告")
def get_all(db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    announcements = announce_show_all(db)
    return success([AnnounceResponse.model_validate(i) for i in announcements])


@announce_router.delete("/{title}", response_model=ResponseModel, summary="删除公告")
def delete_announce(title: str, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    if user["role"] != "admin":
        return error(403, "只有管理员能删除")
    announce_delete(db, title)
    return success("删除成功")


@announce_router.put("/{title}", response_model=ResponseModel[AnnounceResponse], summary="修改公告")
def update_announce(title: str, content: str, auther: str, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    if user["role"] != "admin":
        return error(403, "只有管理员能修改")
    announcement = announce_update(db, title, content, auther)
    return success(AnnounceResponse.model_validate(announcement))
