from pydantic import BaseModel


class AnnounceResponse(BaseModel):
    title: str
    content: str
    author: str
    date: str

    model_config = {
        "from_attributes": True
    }


class AnnounceCreate(BaseModel):
    title: str
    content: str
    author: str
