from fastapi import HTTPException, status
from db.client import db_client
import random
import string

base_url = 'yarilink/'

def create_random_url() -> str:
    count = 0
    found = None
    while found or count <= 5:
        new_id = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        found = db_client.links.find_one({'small_url': new_id})
        count += 1
    
    if found:
        raise HTTPException(status_code=status.HTTP_504_GATEWAY_TIMEOUT,
                            detail='Links Satured')

    return new_id