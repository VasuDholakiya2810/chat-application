""" Logout Resource """

from flask import redirect, url_for, make_response
from flask_restful import Resource
from flask_login import login_required, logout_user


class LogOut(Resource):
    @classmethod
    @login_required
    def get(cls):
        logout_user()
        return make_response(redirect(url_for('login_page')))
