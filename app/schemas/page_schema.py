from pydantic import BaseModel
from typing import List, TypeVar, Generic
T = TypeVar('T')


class PageResponse(BaseModel, Generic[T]):
    page: int
    size: int
    total: int
    items: List[T]
