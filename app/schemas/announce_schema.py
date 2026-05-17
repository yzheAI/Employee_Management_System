from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class AnnounceResponse(BaseModel):
    title: str
    content: str
    author: str
    date: datetime
    is_deleted: bool
    deleted_at: Optional[datetime] = None

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
