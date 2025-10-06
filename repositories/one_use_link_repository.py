from bson import ObjectId
from db.client import db_client
from models.one_use_link import OneUseLink
from models.user import User

class OneUseLinkReposity:

    def __init__(self):
        self.db_client = db_client.oneuse_links

    def find_by_id(self, id: str):
        return self.db_client.find_one({'_id': ObjectId(id)})
    
    def search_by_id_and_redirect_url(self, user_id: str, redirect_url: str):
        return self.db_client.find_one({'user_id': user_id, 'redirect_url': redirect_url}) 
    
    def insert_one_link(self, link: OneUseLink):
        return self.db_client.insert_one(dict(link)).inserted_id
    
    def get_links_of_user(self, user: User):
        return self.db_client.find({'user_id': str(user.id)})
    
    def find_redirect_link(self, small_url: str):
        return self.db_client.find_one({'small_url': small_url})

    def delete_link_by_id(self, id: str):
        return self.db_client.delete_one({'_id': ObjectId(id)})

db_oneuse_link = OneUseLinkReposity()