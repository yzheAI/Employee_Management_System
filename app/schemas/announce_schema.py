from pydantic import BaseModel
from datetime import datetime
from typing import Optional, TypeVar, Generic, List

T = TypeVar('T')


class AnnounceResponse(BaseModel):
    title: str
    content: str
    author: str
    date: datetime

    model_config = {
        "from_attributes": True
    }


class AnnounceCreate(BaseModel):
    title: str
    content: str
    author: str


class AnnounceUpdate(BaseModel):
    title: str
    content: str
    author: str
