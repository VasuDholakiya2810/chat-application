""" model class for room_members """
from typing import List

from db import chat_db

room_member_collection = chat_db.get_collection('room_members')


def create_room_members(room_name:str, username:str):
    room_member_collection.insert_one({"_id": {"room_name": room_name, "username": username}})


def check_user_in_room(room_name:str, username:str):
    return room_member_collection.find_one({"_id": {"room_name": room_name, "username": username}}) or None


def room_for_member(username:str) -> List['room_member_collection']:
    return list(room_member_collection.find({"_id.username": username})) or None
