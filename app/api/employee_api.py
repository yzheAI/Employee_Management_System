from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.security import get_current_user
from app.core.response import error, success
from app.db.crud.employee_crud import employee_get, employee_create, employee_delete, employee_all
from app.db.session import get_db
from app.schemas.employee_schema import EmployeeCreate, EmployeeResponse
from app.schemas.response_schema import ResponseModel
employee_router = APIRouter(prefix="/employees", tags=["员工"])


@employee_router.post("/create", response_model=ResponseModel[EmployeeResponse],summary="员工登记")
async def employee_register(
        employee: EmployeeCreate,
        db: Session = Depends(get_db),
        user: dict = Depends(get_current_user)
):
    if user["role"] != "admin":
        return error(code=403, message="Only Admin can register employee")
    e = employee_create(db, employee.name, employee.age, employee.gender, employee.department_id,employee.role)
    return success(EmployeeResponse.model_validate(e))


@employee_router.get("/find/{id}", response_model=ResponseModel[EmployeeResponse], summary="查找员工")
async def employee_find(employee_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    e = employee_get(db, employee_id)
    if not e:
        return error(code=404, message="Employee not found")
    return success(EmployeeResponse.model_validate(e))


@employee_router.get("/all", response_model=ResponseModel[list[EmployeeResponse]], summary="员工列表")
async def employ_all(db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    employees = employee_all(db)
    return success([EmployeeResponse.model_validate(i) for i in employees])


@employee_router.delete("/delete/{id}", response_model=ResponseModel, summary="删除员工")
async def employee_delete(employee_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    if user["role"] != "admin":
        return error(code=403, message="Only Admin can delete employee")
    if not employee_delete(db, employee_id):
        return error(code=404, message="Employee not found")
    return success(message="Employee deleted")


