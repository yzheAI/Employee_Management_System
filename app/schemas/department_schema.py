from typing import Optional

from pydantic import BaseModel


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
