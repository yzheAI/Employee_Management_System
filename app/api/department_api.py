from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.security import get_current_user
from app.core.response import error, success
from app.db.crud.department_crud import department_get, department_create, department_all, department_delete
from app.db.session import get_db
from app.schemas.department_schema import DepartmentResponse, DepartmentCreate
from app.schemas.response_schema import ResponseModel

department_router = APIRouter(prefix='/departments', tags=['部门'])


@department_router.post('/', response_model=ResponseModel[DepartmentResponse], summary="添加部门")
async def create_department(
        department: DepartmentCreate,
        db: Session = Depends(get_db),
        user: dict = Depends(get_current_user)
):
    if user["role"] != "admin":
        return error(code=403, message="Only Admin can create Department")
    d = department_create(db, department.name, department.description)
    return success(DepartmentResponse.model_validate(d))


@department_router.get('/', response_model=ResponseModel[list[DepartmentResponse]], summary="获取所有部门")
async def get_all_departments(
        db: Session = Depends(get_db),
        user: dict = Depends(get_current_user)
):
    d = department_all(db)
    return success([DepartmentResponse.model_validate(i) for i in d])


@department_router.get('/{department_id}', response_model=ResponseModel[DepartmentResponse], summary="查询部门")
async def get_department(
        department_id: int,
        db: Session = Depends(get_db),
        user: dict = Depends(get_current_user)
):
    d = department_get(db, department_id)
    return success(DepartmentResponse.model_validate(d))


@department_router.delete('/{department_id}', response_model=ResponseModel, summary="删除部门")
async def delete_department(
        d_id: int,
        db: Session = Depends(get_db),
        user: dict = Depends(get_current_user)
):
    if user["role"] != "admin":
        return error(code=403, message="Only Admin can delete Department")
    department_delete(db, d_id)
    return success("Department deleted")
