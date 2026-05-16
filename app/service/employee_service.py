from sqlalchemy.orm import Session
from app.core.exceptions import PermissionDenied, NotFoundError
from app.db.crud.employee_crud import (employee_update, employee_create, employee_delete,
                                       get_employee_department, employee_get, employee_search)


def employee_update_service(
        db: Session,
        user: dict,
        employee_id: int,
        name: str,
        age: int,
        gender: str,
        department_id: int,
        role: str
):
    if user["role"] != "admin":
        raise PermissionDenied("只有管理员能更新")

    employee = employee_update(db, employee_id, name, age, gender, department_id, role)
    return employee


def employee_register_service(
        db: Session,
        user: dict,
        name: str,
        age: int,
        gender: str,
        department_id: int,
        role: str
):
    if user["role"] != "admin":
        raise PermissionDenied("只有管理员能添加")
    e = employee_create(db, name, age, gender, department_id, role)
    return e


def employee_delete_service(
        db: Session,
        user: dict,
        employee_id: int,
):
    if user["role"] != "admin":
        raise PermissionDenied("只有管理员能删除")
    employee_delete(db, employee_id)


def employee_find_department_service(db: Session, employee_id: int):
    department = get_employee_department(db, employee_id)
    if not department:
        raise NotFoundError("未找到该部门")
    return department


def employee_find_service(db: Session, employee_id: int):
    employee = employee_get(db, employee_id)
    return employee


def employees_search_service(db: Session, name: str, age: int, gender: str, role: str, order_by: str, order: str,
                             page: int, size: int):
    employees = employee_search(db, name, age, gender, role, order_by, order, page, size)
    return employees
