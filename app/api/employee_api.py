from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.security import get_current_user
from app.core.response import error, success
from app.db.crud.employee_crud import employee_get, employee_create, employee_delete, employee_all
from app.db.crud.employee_crud import get_employee_department
from app.db.session import get_db
from app.schemas.department_schema import DepartmentResponse
from app.schemas.employee_schema import EmployeeCreate, EmployeeResponse
from app.schemas.response_schema import ResponseModel
employee_router = APIRouter(prefix="/employees", tags=["员工"])


@employee_router.post("/", response_model=ResponseModel[EmployeeResponse],summary="员工登记")
async def employee_register(
        employee: EmployeeCreate,
        db: Session = Depends(get_db),
        user: dict = Depends(get_current_user)
):
    if user["role"] != "admin":
        return error(code=403, message="Only Admin can register employee")
    e = employee_create(db, employee.name, employee.age, employee.gender, employee.department_id,employee.role)
    return success(EmployeeResponse.model_validate(e))


@employee_router.get("/{employee_id}", response_model=ResponseModel[EmployeeResponse], summary="查找员工")
async def employee_find(employee_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    e = employee_get(db, employee_id)
    return success(EmployeeResponse.model_validate(e))


@employee_router.get("/", response_model=ResponseModel[list[EmployeeResponse]], summary="员工列表")
async def employ_all(db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    employees = employee_all(db)
    return success([EmployeeResponse.model_validate(i) for i in employees])


@employee_router.delete("/{employee_id}", response_model=ResponseModel, summary="删除员工")
async def delete_employee(employee_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    if user["role"] != "admin":
        return error(code=403, message="Only Admin can delete employee")
    employee_delete(db, employee_id)
    return success(message="Employee deleted")


@employee_router.get("/department/{employee_id}", response_model=ResponseModel[DepartmentResponse], summary="查找所在部门")
async def find_employee_department(employee_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    department = get_employee_department(db, employee_id)
    if not department:
        return error(code=404, message="Department not found")
    return success(DepartmentResponse.model_validate(department))
