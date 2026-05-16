from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.security import get_current_user
from app.core.response import success
from app.db.session import get_db
from app.schemas.department_schema import DepartmentResponse
from app.schemas.employee_schema import EmployeeCreate, EmployeeResponse, EmployeeUpdate, PageEmployee
from app.schemas.response_schema import ResponseModel
from app.service.employee_service import (employee_delete_service, employee_register_service, employee_update_service,
                                          employee_find_department_service, employee_find_service,
                                          employees_find_service, employees_search_service)
employee_router = APIRouter(prefix="/employees", tags=["员工"])


@employee_router.post("/", response_model=ResponseModel[EmployeeResponse], summary="员工登记")
async def employee_register(
        employee: EmployeeCreate,
        db: Session = Depends(get_db),
        user: dict = Depends(get_current_user)
):
    e = employee_register_service(
        db,
        user,
        employee.name,
        employee.age,
        employee.gender,
        employee.department_id,
        employee.role
    )
    return success(EmployeeResponse.model_validate(e))


@employee_router.get("/{employee_id}", response_model=ResponseModel[EmployeeResponse], summary="查找员工")
async def employee_find(employee_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    e = employee_find_service(db, employee_id)
    return success(EmployeeResponse.model_validate(e))


@employee_router.get("/", response_model=ResponseModel[PageEmployee[EmployeeResponse]], summary="员工列表")
async def employee_all(
        db: Session = Depends(get_db), page: int = 1, size: int = 10, user: dict = Depends(get_current_user)):
    result = employees_find_service(db, page, size)
    return success(result)


@employee_router.delete("/{employee_id}", response_model=ResponseModel, summary="删除员工")
async def delete_employee(employee_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    employee_delete_service(db, user, employee_id)
    return success(message="Employee deleted")


@employee_router.get("/department/{employee_id}", response_model=ResponseModel[DepartmentResponse], summary="查找所在部门")
async def find_employee_department(
        employee_id: int,
        db: Session = Depends(get_db),
        user: dict = Depends(get_current_user)
):
    department = employee_find_department_service(db, employee_id)
    return success(DepartmentResponse.model_validate(department))


@employee_router.put("/{employee_id}", response_model=ResponseModel[EmployeeResponse], summary="修改员工信息")
async def update_employee(
        employee_id: int,
        employee: EmployeeUpdate,
        db: Session = Depends(get_db),
        user: dict = Depends(get_current_user)
):
    employee = employee_update_service(
        db,
        user,
        employee_id,
        employee.name,
        employee.age,
        employee.gender,
        employee.department_id,
        employee.role
    )
    return success(EmployeeResponse.model_validate(employee))


@employee_router.get('/search/{keyword}', response_model=ResponseModel[list[EmployeeResponse]],summary="模糊查询")
async def search_employees(keyword: str, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    employees = employees_search_service(db, keyword)
    return success([EmployeeResponse.model_validate(i) for i in employees])

