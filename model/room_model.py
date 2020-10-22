""" Model class for Room"""
from typing import List

from db import chat_db
from model.room_members import create_room_members

room_collection = chat_db.get_collection('rooms')


def create_room(room_name:str, username:str) -> None:
    room_collection.insert_one({"_id": room_name})
    create_room_members(room_name, username)


def get_room(room_name:str) -> List["room_collection"]:
    return room_collection.find_one({"_id": room_name})
