from fastapi import APIRouter, Depends, HTTPException, status
from models.link import LinkCreate, Link, LinkDB
from models.user import User
from logic.jwt_auth_user import auth_user
from bson import ObjectId
from logic.create_random_link import create_random_url
from schemas.link_schema import link_schema
from repositories.link_repository import db_links
from repositories.user_repository import db_users
from datetime import datetime

router = APIRouter(prefix='/links',
                   tags=['Links'],
                   responses={status.HTTP_404_NOT_FOUND: {'message': 'Not Found'}})

@router.post('/create_link', response_model=LinkDB, status_code=status.HTTP_201_CREATED)
async def create_link(link: LinkCreate, user: User = Depends(auth_user)):

    # The user dont have more than 50 links
    if user.links_count >= 50:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail='User have the limit of urls. UPGRADE YOUR PLAN')

    if not user.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='User is incorrect')
    
    found = db_links.search_by_id_and_redirect_url(user.id, link.redirect_url)

    if found:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail='Link already exists in user account')
   
    
    new_link_db = Link(user_id=user.id,
                       redirect_url=link.redirect_url,
                       small_url=create_random_url(),
                       create_at=str(datetime.utcnow()))

    new_link_id = db_links.insert_one_link(new_link_db)

    created_link = db_links.find_by_id(new_link_id)

    if not created_link:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail='Cannot create in database')
    
    created_link = LinkDB(**link_schema(created_link))

    db_users.update_links_count(user, 1)

    return created_link
