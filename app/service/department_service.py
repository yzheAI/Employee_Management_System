from sqlalchemy.orm import Session
from app.db.crud.department_crud import (
    department_get, department_delete, department_update, department_create, get_department_employees,
    department_search)


def department_create_service(db: Session, name: str, description: str):
    department = department_create(db, name, description)
    return department


def department_delete_service(db: Session, department_id: int):
    department_delete(db, department_id)


def department_update_service(db: Session, department_id: int, name: str, description: str):
    department = department_update(db, department_id, name, description)
    return department


def department_get_service(db: Session, department_id: int):
    department = department_get(db, department_id)
    return department


def department_get_employees_service(db: Session, department_id: int):
    employees = get_department_employees(db, department_id)
    return employees


def department_search_service(db: Session, name: str, description: str, page: int, size: int):
    employees = department_search(db, name, description, page, size)
    return employees
