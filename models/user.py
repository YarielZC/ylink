from typing import Optional
from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    username: str
    email: str
    password: str
    links_count: int = 0

class User(BaseModel):
    id: Optional[str]
    name: str
    username: str
    email: str
    links_count: int
    
class UserDB(User):
    password: str