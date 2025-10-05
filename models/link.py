from typing import Optional
from pydantic import BaseModel

class LinkCreate(BaseModel):
    redirect_url: str

class LinkDB(LinkCreate):
    id: Optional[str]
    user_id: str
    small_url: str
    create_at: str


class Link(LinkCreate):
    user_id: str
    small_url: str
    create_at: str

