""" User Home/Dashboard Resource """

from flask_restful import Resource
from flask import render_template, make_response
from flask_login import login_required, current_user

from model.room_members import room_for_member


class Home(Resource):
    @classmethod
    @login_required
    def get(cls):
        rooms = room_for_member(current_user.username)
        return make_response(render_template('home.html', username=current_user.username, rooms=rooms))
