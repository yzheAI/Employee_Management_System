from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.response import success
from app.core.security import get_current_user
from app.db.session import get_db
from app.schemas.response_schema import ResponseModel
from app.schemas.announce_schema import AnnounceResponse, AnnounceCreate
from app.schemas.page_schema import PageResponse
from app.service.announce_service import announce_create_service, announce_delete_service, announce_update_service, \
    announce_find_service,  announce_search_service

announce_router = APIRouter(prefix="/announcement", tags=["公告"])


@announce_router.post("/", response_model=ResponseModel[AnnounceResponse], summary="添加公告")
def create_announce(announce: AnnounceCreate, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    a = announce_create_service(db, announce.title, announce.content, announce.author, user)
    return success(AnnounceResponse.model_validate(a))


@announce_router.get("/search", response_model=ResponseModel[PageResponse[AnnounceResponse]],
                     summary="公告列表（支持分页 + 模糊查询）")
def search_announce(
        keyword: str = "",
        page: int = 1,
        size: int = 10,
        db: Session = Depends(get_db),
        user: dict = Depends(get_current_user)
):
    announcements = announce_search_service(db, keyword, page, size)
    return success(announcements)


@announce_router.get("/{title}", response_model=ResponseModel[AnnounceResponse], summary="查找公告")
def get_announce(title: str, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    announce_db = announce_find_service(db, title)
    return success(AnnounceResponse.model_validate(announce_db))


@announce_router.delete("/{title}", response_model=ResponseModel, summary="删除公告")
def delete_announce(title: str, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    announce_delete_service(db, title, user)
    return success("删除成功")


@announce_router.put("/{title}", response_model=ResponseModel[AnnounceResponse], summary="修改公告")
def update_announce(announce: AnnounceResponse, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    announcement = announce_update_service(db, announce.title, announce.content, announce.author, user)
    return success(AnnounceResponse.model_validate(announcement))
