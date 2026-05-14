import bcrypt
from sqlalchemy.orm import Session

from app.models.user import User


def create_user(db: Session, username, password, role="user"):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    user = User(
        username=username,
        password=hashed_password.decode('utf-8'),
        role=role
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user(db: Session, username: str):
    user = db.query(User).filter(User.username == username).first()
    return user


def verify_user(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
