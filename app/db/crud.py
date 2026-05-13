from app.models.announcement import Announcement
from app.models.student import Student
from app.models.user import User
from sqlalchemy.orm import Session
from datetime import datetime
import bcrypt


def create_student(db: Session, name: str, sex: str, age: int, s_id: str, score: int) -> Student:
    student = Student(name=name, sex=sex, age=age, s_id=s_id, score=score)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student


def get_student(db: Session, s_id: str):
    return db.query(Student).filter(Student.s_id == s_id).first()


def get_all(db: Session) -> list:
    return db.query(Student).all()


def delete_student(db: Session, s_id: str) -> bool:
    student = get_student(db, s_id)
    if not student:
        return False
    db.delete(student)
    db.commit()
    return True


def update_student(db: Session, student_id: str, **kwargs):
    """
    kwargs: 只包含需要更新的字段
    自动过滤 None，未传字段不会被覆盖
    """
    student = get_student(db, student_id)
    if not student:
        return None
    for key, value in kwargs.items():
        if value is not None:
            setattr(student, key, value)
    db.commit()
    db.refresh(student)
    return student


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


def announce_create(db: Session, title: str, content: str, author: str):
    now = str(datetime.utcnow())
    announcement = Announcement(
        title=title,
        content=content,
        author=author,
        date=now
    )
    db.add(announcement)
    db.commit()
    db.refresh(announcement)
    return announcement


def announce_find(db: Session, title: str):
    announce = db.query(Announcement).filter(Announcement.title == title).first()
    return announce


def announce_show_all(db: Session):
    announces = db.query(Announcement).all()
    return announces


def announce_delete(db: Session, announce_id) -> bool:
    announce = announce_find(db, announce_id)
    if not announce:
        return False
    db.delete(announce)
    db.commit()
    return True
