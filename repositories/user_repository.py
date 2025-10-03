from db.client import db_client
from models.user import User, UserCreate
from bson import ObjectId



class UserRepository:

    def __init__(self):
        self.db_client = db_client.users

    def find_by_field(self, field: 'str', value):
        return self.db_client.find_one({field: value})

    def find_by_id(self, id: str):
        return self.db_client.find_one({'_id': ObjectId(id)})
    
    def insert_one_user(self, user: UserCreate):
        return self.db_client.insert_one(dict(user)).inserted_id
    
    def insert_one_user_with_dict(self, user: dict):
        return self.db_client.insert_one(user).inserted_id

    def update_links_count(self, user: User, add_count: int):
        return self.db_client.update_one({'_id': ObjectId(user.id)}, {
            '$set': {
                'links_count': user.links_count + add_count
            }
        })
db_users = UserRepository()