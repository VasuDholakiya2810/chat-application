import os
from pymongo import MongoClient

client = MongoClient(os.getenv('DATABASE_URL'))

chat_db = client.get_database('ChatApplication')

