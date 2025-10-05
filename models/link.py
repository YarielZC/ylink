from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class LinkCreate(BaseModel):
    redirect_url: str

class LinkDB(LinkCreate):
    id: Optional[str]
    user_id: str
    small_url: str
    touch_counts: int = 0
    create_at: str = str(datetime.utcnow())


class Link(LinkCreate):
    user_id: str
    small_url: str
    touch_counts: int = 0
    create_at: str = str(datetime.utcnow())

