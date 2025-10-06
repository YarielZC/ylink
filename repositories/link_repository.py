from db.client import db_client
from models.link import LinkCreate, LinkDB
from bson import ObjectId

from models.user import User



class LinkRepository:

    def __init__(self):
        self.db_client = db_client.links

    def find_by_id(self, id: str):
        return self.db_client.find_one({'_id': ObjectId(id)})
    
    def search_by_id_and_redirect_url(self, user_id: str, redirect_url: str):
        return self.db_client.find_one({'user_id': user_id, 'redirect_url': redirect_url})
    
    def find_by_field(self, field: 'str', value):
        return self.db_client.find_one({field: value})
    
    def find_redirect_link(self, small_url: str):
        return self.db_client.find_one({'small_url': small_url})
    
    def insert_one_link(self, link: LinkCreate):
        return self.db_client.insert_one(dict(link)).inserted_id

    def get_links_of_user(self, user: User):
        return self.db_client.find({'user_id': str(user.id)})

    def update_touch_link_count(self, link: LinkDB):
        return self.db_client.update_one({'_id': ObjectId(link.id)}, {
            '$set': {
                'touch_counts': link.touch_counts + 1
            }
        })
db_links = LinkRepository()