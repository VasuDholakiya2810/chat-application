""" model class for date in message """
from datetime import datetime

from db import chat_db

date_collection = chat_db.get_collection('dates')


def save_date(date: datetime, room: str):
    date_collection.insert_one({"date": date, "room": room})


def get_date(room_name: str):
    return list(date_collection.find({"room": room_name}))


def check_date(date: datetime, room: str):
    return date_collection.find_one({"date": date, "room": room}) or None
