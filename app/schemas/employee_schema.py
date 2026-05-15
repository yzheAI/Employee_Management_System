from pydantic import BaseModel
from typing import Optional, Generic, TypeVar, List
T = TypeVar('T')


class EmployeeCreate(BaseModel):
    name: str
    age: int
    gender: str
    department_id: int
    role: str = "staff"


class EmployeeResponse(BaseModel):
    id: int
    name: str
    age: int
    gender: str
    department_id: int
    role: str = "staff"

    model_config = {
        "from_attributes": True
    }


class EmployeeUpdate(BaseModel):
    name: str
    age: int
    gender: str
    department_id: int
    role: str


class PageEmployee(BaseModel, Generic[T]):
    page: int
    size: int
    total: int
    items: List[T]
