from datetime import datetime

from pydantic import BaseModel
from typing import Optional

from app.models.department import Department


class EmployeeCreate(BaseModel):
    name: str
    age: int
    gender: str
    department_id: int
    role: str = "staff"


class DepartmentMini(BaseModel):
    id: int
    name: str

    model_config = {
        "from_attributes": True
    }


class EmployeeResponse(BaseModel):
    id: int
    name: str
    age: int
    gender: str
    department_id: int
    role: str
    is_deleted: bool
    deleted_at: Optional[datetime] = None
    department: Optional[DepartmentMini] = None

    model_config = {
        "from_attributes": True
    }


class EmployeeUpdate(BaseModel):
    name: str
    age: int
    gender: str
    department_id: int
    role: str
