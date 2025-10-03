import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from db.client import db_client
from models.user import User
from schemas.user_schema import user_schema
from config import Settings
from functools import lru_cache
from typing import Annotated

oauth2 = OAuth2PasswordBearer(tokenUrl='/login')

@lru_cache
def get_settings():
    return Settings()

async def auth_user(settings: Annotated[Settings, Depends(get_settings)], token: str = Depends(oauth2)):

    unauthorized_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalide credentials",
                            headers={"WWW-Authenticate": 'Bearer'})
    try:
        user = jwt.decode(token, settings.SECRET_TOKEN_KEY, settings.ALGORITHM_CRYPT).get('sub')
        
    except:
        raise unauthorized_exception
    if not user:
        raise unauthorized_exception
    
    user_db = db_client.users.find_one({'username': user})

    if not user_db:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='User not is registered')

    user_db = User(**user_schema(user_db))

    return user_db