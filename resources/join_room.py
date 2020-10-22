""" Join Room Resource """
from flask_restful import Resource
from flask import make_response, render_template
from flask_login import login_required

from common.constant import HEADERS

class JoinRoom(Resource):
    @classmethod
    @login_required
    def get(cls):
        return make_response(render_template('join_room.html'),HEADERS)




