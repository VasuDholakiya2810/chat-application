""" model class for messages """
from datetime import datetime

from db import chat_db

message_collection = chat_db.get_collection('messages')


def save_message(message: str, username: str, room: str, date: datetime, time: datetime):
    message_collection.insert_one({"text": message, "username": username, "date": date, "time": time, "room": room})


def get_message(date: datetime, room: str):
    return list(message_collection.find({"date": date, "room": room}))
