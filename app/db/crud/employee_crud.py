from sqlalchemy.orm import Session
from app.core.exceptions import ConflictError, NotFoundError
from app.models.department import Department
from app.models.employee import Employee
from app.schemas.employee_schema import EmployeeResponse
from utils.pagination import paginate


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


def employee_delete(db: Session, employee_id: int):
    employee = employee_get(db, employee_id)
    db.delete(employee)
    db.commit()
    return True


def get_employee_department(db: Session, employee_id: int):
    employee = employee_get(db, employee_id)
    department = employee.department
    return department


def employee_update(
        db: Session,
        employee_id: int,
        name: str,
        age: int,
        gender: str,
        department_id: int,
        role: str
):

    employee = employee_get(db, employee_id)
    if not db.query(Department).filter(Department.id == department_id).first():
        raise NotFoundError('Department does not exist')
    employee.name = name
    employee.age = age
    employee.gender = gender
    employee.department_id = department_id
    employee.role = role
    db.commit()
    db.refresh(employee)
    return employee


def employee_search(db: Session, name: str, age: int, gender: str, role: str, page: int, size: int):
    query = db.query(Employee)
    if name.strip():
        query = query.filter(Employee.name.like(f'%{name}%'))
    if age is not None:
        query = query.filter(Employee.age == age)
    if gender.strip():
        query = query.filter(Employee.gender == gender)
    if role.strip():
        query = query.filter(Employee.role == role)
    result = paginate(query, page, size, EmployeeResponse)
    return result
