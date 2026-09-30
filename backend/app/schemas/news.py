from pydantic import BaseModel
from typing import Optional


class NewsCreate(BaseModel):
    title: str
    content: str
    source: str
    url: Optional[str] = None


class NewsOut(BaseModel):
    id: int
    title: str
    content: str
    source: str
    url: Optional[str] = None

    class Config:
        from_attributes = True
