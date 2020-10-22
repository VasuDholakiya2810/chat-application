""" Login Resource """
from flask_restful import Resource
from flask import render_template, make_response, redirect, request, url_for, session
from flask_login import current_user, login_user

from common.constant import HEADERS, USER_NOT_EXISTS
from model.user import get_user


class LoginPage(Resource):
    @classmethod
    def get(cls):
        if current_user.is_authenticated:
            return redirect(url_for('home_page'))
        return make_response(render_template('index.html'), HEADERS)

    @classmethod
    def post(cls):
        username = request.form.get('username')
        email = request.form.get('email')
        user = get_user(username)

        if user and user.email == email:
            login_user(user)
            session['username']=username
            resp= make_response(redirect(url_for('home_page')))
            resp.set_cookie('username',username)
            return resp

        return make_response(render_template('index.html', message=USER_NOT_EXISTS), HEADERS)
