from fastapi import FastAPI, HTTPException, status
from fastapi.responses import RedirectResponse
from api import register_user, login, links, users
from models.link import LinkDB
from models.one_use_link import OneUseLinkDB
from schemas.link_schema import link_schema
from schemas.one_use_link_schema import one_use_link_schema
from repositories.link_repository import db_links
from repositories.one_use_link_repository import db_oneuse_link

app = FastAPI()

app.include_router(register_user.router)
app.include_router(login.router)
app.include_router(links.router)
app.include_router(users.router)

@app.get('/{small_url}', response_class=RedirectResponse)
async def redirect(small_url: str):

    not_found_exception = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='URL invalid or not found')
    redirect_url = ''

    # For Normals Links (their small url have 5 characters)
    if len(small_url) == 5:
        found = db_links.find_redirect_link(small_url)
        
        if not found:
            raise not_found_exception
        
        linkDB = LinkDB(**link_schema(found))
        redirect_url = linkDB.redirect_url
        db_links.update_touch_link_count(linkDB)

        
    # For One Use Links (their small url have 6 characters)
    elif len(small_url) == 6:
        found = db_oneuse_link.find_redirect_link(small_url)
        if not found:
            raise not_found_exception
    
        oneuse_linkDB = OneUseLinkDB(**one_use_link_schema(found))
        redirect_url = oneuse_linkDB.redirect_url
        db_oneuse_link.delete_link_by_id(str(oneuse_linkDB.id))
        
    else:
        raise not_found_exception
    

  
    return RedirectResponse(redirect_url)