from sqlalchemy.orm import Session

from app.core.response import error
from app.models.department import Department
from app.models.employee import Employee


def employee_create(db: Session, name: str, age: int, gender: str, department_id: int, role: str):
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
