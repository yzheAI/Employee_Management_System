from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.response import error, success
from app.core.security import get_current_user
from app.db.session import get_db
from app.schemas.response_schema import ResponseModel
from app.schemas.announce_schema import AnnounceResponse, AnnounceCreate
from app.db.crud import announce_create, announce_delete, announce_find, announce_show_all
announce_router = APIRouter(prefix="/announcement", tags=["announcement"])


@announce_router.post("/add/", response_model=ResponseModel[AnnounceResponse], summary="添加公告")
def create_announce(announce: AnnounceCreate, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    announce_db = announce_find(db, announce.title)
    if user["role"] != "admin":
        return error(404, "只有管理员能添加")
    if announce_db:
        return error(404, "标题已存在")
    a = announce_create(db, announce.title, announce.content, announce.author)
    return success(AnnounceResponse.model_validate(a))


@announce_router.get("/find/", response_model=ResponseModel[AnnounceResponse], summary="查找公告")
def get_announce(title: str, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    announce_db = announce_find(db, title)
    if not announce_db:
        return error(404, "没有该公告")
    return success(AnnounceResponse.model_validate(announce_db))


@announce_router.get("/all/", response_model=ResponseModel[list[AnnounceResponse]], summary="获取所有公告")
def get_all(db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    announcements = announce_show_all(db)
    return success([AnnounceResponse.model_validate(i) for i in announcements])


@announce_router.delete("/delete/", response_model=ResponseModel, summary="删除公告")
def delete_announce(title: str, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    if user["role"] != "admin":
        return error(404, "只有管理员能删除")
    if not announce_delete(db, title):
        return error(404, "没有该公告")
    return success("删除成功")
