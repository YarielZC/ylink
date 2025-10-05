from fastapi import FastAPI, HTTPException, status
from fastapi.responses import RedirectResponse
from api import register_user, login, links, users
from models.link import LinkDB
from schemas.link_schema import link_schema
from repositories.link_repository import db_links

app = FastAPI()

app.include_router(register_user.router)
app.include_router(login.router)
app.include_router(links.router)
app.include_router(users.router)

@app.get('/{small_url}')
async def redirect(small_url: str):

    found = db_links.find_redirect_link(small_url)
    # print(small_url)
    if not found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='URL invalid or not found')

    linkDB = LinkDB(**link_schema(found))
    redirect_url = linkDB.redirect_url

    db_links.update_touch_link_count(linkDB)

    return RedirectResponse(redirect_url)