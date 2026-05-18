from datetime import datetime

from sqlalchemy.orm import Session
from app.core.exceptions import ConflictError, NotFoundError
from app.models.department import Department
from app.models.employee import Employee
from app.schemas.department_schema import DepartmentResponse
from utils.pagination import paginate
from utils.query_builder import apply_filters, base_query


def department_get(db: Session, department_id: int):
    query = base_query(db, Department)
    department_db = query.filter(Department.id == department_id).first()
    if not department_db:
        raise NotFoundError(f"Department with id {department_id} not found")
    return department_db


def department_create(db: Session, department_name: str, description: str):
    department_db = base_query(db, Department).filter(Department.name == department_name).first()
    if department_db:
        raise ConflictError(f"Department with name '{department_name}' already exists")
    department = Department(name=department_name, description=description)
    db.add(department)
    db.commit()
    db.refresh(department)
    return department


def department_delete(db: Session, department_id: int):
    department = department_get(db, department_id)
    if get_department_employees(db, department_id):
        raise ConflictError("employees exist")
    department.is_deleted = True
    department.deleted_at = datetime.utcnow()
    db.commit()
    return True


def department_update(db: Session, department_id: int, name, description: str):
    department = department_get(db, department_id)
    department.name = name
    department.description = description
    db.commit()
    db.refresh(department)
    return department


def get_department_employees(db: Session, department_id: int):
    query = base_query(db, Employee)
    employees = query.filter(Employee.department_id == department_id).all()
    return employees


def department_search(db: Session, name: str, description: str, page: int, size: int):
    query = base_query(db, Department)

    conditions = []

    if name.strip():
        conditions.append(
            Department.name.ilike(f"%{name}%")
        )
    if description.strip():
        conditions.append(
            Department.description.ilike(f"%{description}%")
        )

    query = apply_filters(query, conditions)

    result = paginate(query, page, size, DepartmentResponse)
    return result
