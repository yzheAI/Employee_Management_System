from sqlalchemy.orm import Session
from app.core.exceptions import ConflictError, NotFoundError
from app.models.department import Department
from app.models.employee import Employee
from app.schemas.department_schema import DepartmentResponse


def department_get(db: Session, department_id: int):
    department_db = db.query(Department).filter(Department.id == department_id).first()
    if not department_db:
        raise NotFoundError(f"Department with id {department_id} not found")
    return department_db


def department_create(db: Session, department_name: str, description: str):
    department_db = db.query(Department).filter(Department.name == department_name).first()
    if department_db:
        raise ConflictError(f"Department with name '{department_name}' already exists")
    department = Department(name=department_name, description=description)
    db.add(department)
    db.commit()
    db.refresh(department)
    return department


def department_delete(db: Session, department_id: int):
    department = department_get(db, department_id)
    db.delete(department)
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
    employees = db.query(Employee).filter(Employee.department_id == department_id).all()
    return employees


def department_search(db: Session, keyword: str, page: int, size: int):
    query = db.query(Department)
    if keyword and keyword.strip():
        query = query.filter(Department.name.ilike(f'%{keyword}%'))
    total = query.count()
    items = query.offset((page - 1) * size).limit(size).all()
    result = {
        "page": page,
        "size": size,
        "total": total,
        "items": [DepartmentResponse.model_validate(i) for i in items]
    }
    return result
