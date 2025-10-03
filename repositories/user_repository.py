from db.client import db_client
from models.user import UserCreate
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

db_users = UserRepository()