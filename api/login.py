from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from repositories.user_repository import db_users
from logic.jwt_auth_user import auth_user
from models.user import UserDB, User
from schemas.user_schema import user_db_schema
import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from config import Settings
from functools import lru_cache

crypt = CryptContext(schemes=['bcrypt'])


router = APIRouter(prefix='/login',
                   tags=['Login'],
                   responses={status.HTTP_404_NOT_FOUND: {'message': 'Not Found'}})

@lru_cache
def get_settings():
    return Settings()

@router.post('/', response_model=dict, status_code=status.HTTP_202_ACCEPTED)
async def login(settings: Annotated[Settings, Depends(get_settings)], form: OAuth2PasswordRequestForm = Depends()):
    # Allow register by username or gmail
    if form.username.find('@gmail.com') != -1:
        user_db = db_users.find_by_field('email', form.username)
    else:
        user_db = db_users.find_by_field('username', form.username)
    
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Username or password is wrong')
    
    user_db = UserDB(**user_db_schema(user_db))

    if not crypt.verify(form.password, user_db.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Username or password is wrong')
    

    access_token_expiration = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_DURATION)
    access_token = {"sub": user_db.username,
                    'exp': access_token_expiration}

    return {'access_token': jwt.encode(access_token, 
                                       key=settings.SECRET_TOKEN_KEY,
                                       algorithm=settings.ALGORITHM_CRYPT), 
            'token_type': 'bearer'}

