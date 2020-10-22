""" Logout Resource """

from flask import redirect, url_for, session, make_response
from flask_restful import Resource
from flask_login import login_required, logout_user



class LogOut(Resource):
    @classmethod
    @login_required
    def get(cls):
        session.pop('username',None)
        logout_user()
        resp= make_response(redirect(url_for('login_page')))
        resp.delete_cookie('username')
        return resp