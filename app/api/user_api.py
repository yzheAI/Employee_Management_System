from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from app.core.permission import require_roles
from app.db.crud.user_crud import create_user, get_user, verify_user
from app.schemas.user_schema import UserRegister, UserLogin, TokenResponse, AdminRegister
from app.db.session import get_db
from app.core.security import get_current_user, login_user
from app.core.response import success, error
from app.schemas.response_schema import ResponseModel
from app.service.user_service import user_register_service, user_login_service, admin_register_service

router = APIRouter(prefix="/users", tags=["用户管理"])


@router.post("/register", summary="用户注册")
async def register(user: UserRegister, db: Session = Depends(get_db)):
    u = user_register_service(db=db, username=user.username, password=user.password)
    return success({
        "username": u.username,
        "role": u.role
    })


@router.post("/admin/register", summary="管理员注册")
async def register_admin(user: AdminRegister, db: Session = Depends(get_db), user_role: dict = Depends(require_roles("admin"))):
    u = admin_register_service(db=db, username=user.username, password=user.password, role=user.role)
    return success({
        "username": u.username,
        "role": u.role
    })


@router.post("/login", summary="用户登录", response_model=ResponseModel[TokenResponse])
async def login(user: UserLogin, db: Session = Depends(get_db)):
    access_token = user_login_service(db=db, username=user.username, password=user.password)
    return success(TokenResponse(access_token=access_token, token_type="Bearer"))


@router.get("/students/")
def get_all(user=Depends(get_current_user)):
    return {"message":  f"Hello, {user}! You have access to this data."}

