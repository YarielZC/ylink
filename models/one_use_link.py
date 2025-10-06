from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class OneUseLinkCreate(BaseModel):
    redirect_url: str

class OneUseLink(OneUseLinkCreate):
    user_id: str
    small_url: str
    create_at: str = str(datetime.utcnow())

class OneUseLinkDB(OneUseLink):
    id: Optional[str]
    

