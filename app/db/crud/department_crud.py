from sqlalchemy.orm import Session

from app.core.response import error
from app.models.department import Department


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
