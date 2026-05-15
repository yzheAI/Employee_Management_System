from pydantic import BaseModel


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
