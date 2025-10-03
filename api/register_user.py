from fastapi import APIRouter, HTTPException, status
from repositories.user_repository import db_users
from models.user import User, UserDB, UserCreate
from logic.validations.register_user_validation import register_user_validate
from schemas.user_schema import user_schema 
from passlib.context import CryptContext

crypt = CryptContext(schemes=['bcrypt'])

router = APIRouter(prefix='/register_user',
                   tags=['Register User'],
                   responses={status.HTTP_404_NOT_FOUND: {'message': 'Not Found'}})

@router.post('/', response_model=User, status_code=status.HTTP_201_CREATED)
async def register_user(user: UserCreate):
    
    register_user_validate(user)

    user_dict = dict(user)

    user_dict['password'] = crypt.hash(user_dict['password'])

    id = db_users.insert_one_user_with_dict(user_dict)

    new_user = user_schema(db_users.find_by_id(id))
    return User(**new_user)
    
    
    