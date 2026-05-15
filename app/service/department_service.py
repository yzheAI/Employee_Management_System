from sqlalchemy.orm import Session

from app.core.exceptions import PermissionDenied
from app.db.crud.department_crud import (
    department_get, department_all, department_delete, department_update, department_create, get_department_employees)


def department_create_service(db: Session, name: str, description: str, user: dict):
    if user["role"] != "admin":
        raise PermissionDenied("管理员才能创建部门")
    department = department_create(db, name, description)
    return department


def department_delete_service(db: Session, department_id: int, user: dict):
    if user["role"] != "admin":
        raise PermissionDenied("管理员才能删除部门")
    department_delete(db, department_id)


def department_update_service(db: Session, department_id: int, name: str, description: str, user: dict):
    if user["role"] != "admin":
        raise PermissionDenied("管理员才能修改")
    department = department_update(db, department_id, name, description)
    return department


def department_get_service(db: Session, department_id: int):
    department = department_get(db, department_id)
    return department


def departments_get_service(db: Session, page, size):
    departments = department_all(db, page, size)
    return departments


def department_get_employees_service(db: Session, department_id: int):
    employees = get_department_employees(db, department_id)
    return employees
