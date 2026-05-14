from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from app.db.crud.user_crud import create_user, get_user, verify_user
from app.schemas.user_schema import UserRegister, UserLogin, TokenResponse
from app.db.session import get_db
from app.core.security import get_current_user, login_user
from app.core.response import success, error
from app.schemas.response_schema import ResponseModel
router = APIRouter(prefix="/users", tags=["用户管理"])


@router.post("/register", summary="用户注册")
async def register(user: UserRegister, db: Session = Depends(get_db)):
    db_user = get_user(db, user.username)
    if db_user:
        return error(400, "用户已存在")
    u = create_user(db, user.username, user.password, user.role)
    return success({
        "username": u.username,
        "role": u.role
    })


@router.post("/login", summary="用户登录", response_model=ResponseModel[TokenResponse])
async def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = get_user(db, user.username)
    if not db_user or not verify_user(user.password, db_user.password):
        raise HTTPException(400, "用户名或密码错误")
    access_token = login_user(db_user)
    return success(TokenResponse(access_token=access_token, token_type="Bearer"))


@router.get("/students/")
def get_all(user=Depends(get_current_user)):
    return {"message":  f"Hello, {user}! You have access to this data."}
