from fastapi import APIRouter, Depends, status
from models.link import Link
from repositories.link_repository import db_links
from models.user import User
from logic.jwt_auth_user import auth_user

router = APIRouter(prefix='/users',
                   tags=['Users'],
                   responses={status.HTTP_404_NOT_FOUND: {'message': 'Not Found'}})

@router.get('/me', response_model=User, status_code=status.HTTP_200_OK)
async def me(user: User = Depends(auth_user)):
    return user

@router.get('/links/me', response_model=list[Link], status_code=status.HTTP_200_OK)
async def get_links_user(user: User = Depends(auth_user)):
    links = db_links.get_links_of_user(user)
    
    return list(links)