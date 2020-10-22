""" Room Resource """

from flask import make_response, render_template, request, url_for,redirect
from flask_login import login_required, current_user
from flask_restful import Resource


from common.constant import HEADERS, ROOM_NOT_EXISTS
from model.room_model import get_room


class ViewRoom(Resource):
    @classmethod
    @login_required
    def get(cls):
        room_name = request.args.get('room_name')
        room = get_room(room_name)
        if room:
            return make_response(
                render_template('view_room.html', room_name=room['_id'], username=current_user.username), HEADERS)

        return make_response(render_template('join_room.html',message=ROOM_NOT_EXISTS.format(room_name)),HEADERS)
