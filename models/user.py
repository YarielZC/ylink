from typing import Optional
from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    username: str
    email: str
    password: str

class User(BaseModel):
    id: Optional[str]
    name: str
    username: str
    email: str
    
class UserDB(User):
    password: str