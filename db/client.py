from pymongo import MongoClient
from config import Settings
from functools import lru_cache

@lru_cache
def get_settings():
    return Settings()


# LOCAL DEVELOPMENT
# db_client = MongoClient().local

#PRODUCTION
db_client = MongoClient(get_settings().URL_DB).ylink