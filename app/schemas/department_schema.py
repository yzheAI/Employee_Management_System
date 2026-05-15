from typing import Optional, List, Generic, TypeVar
from pydantic import BaseModel
T = TypeVar('T')


class DepartmentCreate(BaseModel):
    name: str
    description: Optional[str]


class DepartmentResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]

    model_config = {
        "from_attributes": True
    }


class PageDepartment(BaseModel, Generic[T]):
    page: int
    size: int
    total: int
    items: List[T]
