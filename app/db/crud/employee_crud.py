from sqlalchemy.orm import Session
from app.core.exceptions import ConflictError, NotFoundError
from app.models.department import Department
from app.models.employee import Employee


def employee_create(db: Session, name: str, age: int, gender: str, department_id: int, role: str):
    if not db.query(Department).filter(Department.id == department_id).first():
        raise NotFoundError('Department does not exist')
    employee = Employee(name=name, age=age, gender=gender, department_id=department_id, role=role)
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee


def employee_get(db: Session, employee_id: int):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise NotFoundError('Employee does not exist')
    return employee


def employee_all(db: Session):
    employees = db.query(Employee).all()
    return employees


def employee_delete(db: Session, employee_id: int):
    employee = employee_get(db, employee_id)
    db.delete(employee)
    db.commit()
    return True


def get_employee_department(db: Session, employee_id: int):
    employee = employee_get(db, employee_id)
    department = employee.department
    return department
