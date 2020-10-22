""" Create Room Resource """
from flask import request, render_template, make_response, redirect, url_for
from flask_login import login_required, current_user
from flask_restful import Resource
from pymongo.errors import DuplicateKeyError

from common.constant import ROOM_ALREADY_EXSITS
from model.room_model import create_room


class CreateRoom(Resource):

    @classmethod
    @login_required
    def get(cls):
        return make_response(render_template('create_room.html'))

    @classmethod
    @login_required
    def post(cls):
        room_name = request.form.get('room_name')
        try:
            create_room(room_name, current_user.username)
            return redirect(url_for('room', room_name=room_name))

        except DuplicateKeyError:
            return make_response(render_template('create_room.html', message=ROOM_ALREADY_EXSITS.format(room_name)))
