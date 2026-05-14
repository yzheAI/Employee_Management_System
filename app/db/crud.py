from app.core.response import error
from app.models.announcement import Announcement
from app.models.department import Department
from app.models.employee import Employee
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


def department_find(db: Session, department_id: int):
    department_db = db.query(Department).filter(Department.id == department_id).first()
    return department_db


def department_create(db: Session, department_name: str, description: str):
    department_db = db.query(Department).filter(Department.name == department_name).first()
    if department_db:
        return error(400, f"Department {department_name} already exists")
    department = Department(name=department_name, description=description)
    db.add(department)
    db.commit()
    db.refresh(department)
    return department


def department_all(db: Session):
    departments = db.query(Department).all()
    return departments


def department_delete(db: Session, department_id: int):
    department = department_find(db, department_id)
    if not department:
        return False
    db.delete(department)
    db.commit()
    return True


def employee_create(db: Session, name: str, age: int, gender: str, department_id: int, role: str):
    if db.query(Employee).filter(Employee.name == name).first():
        return error(400, message="Employee already exists")
    if not db.query(Department).filter(Department.id == department_id).first():
        return error(404, "Department not found")
    employee = Employee(name=name, age=age, gender=gender, department_id=department_id, role=role)
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee


def employee_get(db: Session, employee_id: int):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    return employee


def employee_all(db: Session):
    employees = db.query(Employee).all()
    return employees


def employee_delete(db: Session, employee_id: int):
    employee = employee_get(db, employee_id)
    if not employee:
        return False
    db.delete(employee)
    db.commit()
    return True
