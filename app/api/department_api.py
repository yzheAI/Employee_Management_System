from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.security import get_current_user
from app.core.response import success
from app.db.session import get_db
from app.schemas.department_schema import DepartmentResponse, DepartmentCreate, PageDepartment
from app.schemas.employee_schema import EmployeeResponse
from app.schemas.response_schema import ResponseModel
from app.service.department_service import (department_create_service, department_delete_service,
                                            department_update_service, department_get_service,
                                            department_get_employees_service, department_search_service)


department_router = APIRouter(prefix='/departments', tags=['部门'])


@department_router.post('/', response_model=ResponseModel[DepartmentResponse], summary="添加部门")
async def create_department(
        department: DepartmentCreate,
        db: Session = Depends(get_db),
        user: dict = Depends(get_current_user)
):
    d = department_create_service(db, department.name, department.description, user)
    return success(DepartmentResponse.model_validate(d))


@department_router.get('/search', response_model=ResponseModel[PageDepartment[DepartmentResponse]], summary="部门列表（支持分页+模糊查询）")
async def search_department(
        keyword: str = "",
        page: int = 1,
        size: int = 10,
        db: Session = Depends(get_db),
        user: dict = Depends(get_current_user)
):
    result = department_search_service(db, keyword, page, size)
    return success(result)


@department_router.get('/{department_id}', response_model=ResponseModel[DepartmentResponse], summary="查询部门")
async def get_department(
        department_id: int,
        db: Session = Depends(get_db),
        user: dict = Depends(get_current_user)
):
    d = department_get_service(db, department_id)
    return success(DepartmentResponse.model_validate(d))


@department_router.delete('/{department_id}', response_model=ResponseModel, summary="删除部门")
async def delete_department(
        department_id: int,
        db: Session = Depends(get_db),
        user: dict = Depends(get_current_user)
):
    department_delete_service(db, department_id, user)
    return success("Department deleted")


@department_router.put('/{department_id}', response_model=ResponseModel[DepartmentResponse], summary="修改部门信息")
async def update_department(
        department_id: int,
        name: str,
        description: str,
        db: Session = Depends(get_db),
        user: dict = Depends(get_current_user)
):
    department = department_update_service(db, department_id, name, description, user)
    return success(DepartmentResponse.model_validate(department))


@department_router.get('/employees/{department_id}', response_model=ResponseModel[list[EmployeeResponse]],
                       summary="获取部门员工")
async def get_employees(department_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    employees = department_get_employees_service(db, department_id)
    return success([EmployeeResponse.model_validate(i) for i in employees])



