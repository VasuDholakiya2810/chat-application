""" model class for user """
from db import chat_db
from flask_login import UserMixin

user_collection = chat_db.get_collection('users')

class User(UserMixin):
    def __init__(self,username,email):
        self.id=username
        self.username=username
        self.email=email



def save_user(username, email):
    user_collection.insert_one({'_id': username, 'email': email})


def get_user(username):
    user_data = user_collection.find_one({'_id': username})
    return User(user_data['_id'], user_data['email']) if user_data else None
