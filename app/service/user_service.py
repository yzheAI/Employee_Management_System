from app.core.security import login_user
from app.db.crud.user_crud import create_user, get_user, verify_user
from sqlalchemy.orm import Session
from app.core.exceptions import PermissionDenied


def user_register_service(db: Session, username: str, password: str):
    user = create_user(db, username, password)
    return user


def admin_register_service(db: Session, username: str, password: str, role: str):
    admin = create_user(db, username, password, role)
    return admin


def user_login_service(db: Session, username: str, password: str):
    db_user = get_user(db, username)
    if not db_user or not verify_user(password, db_user.password):
        raise PermissionDenied("账户或密码错误")
    access_token = login_user(db_user)
    return access_token




