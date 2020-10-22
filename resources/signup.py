""" Signup Resource """
from flask_restful import Resource
from flask import render_template, request, make_response
from pymongo.errors import DuplicateKeyError

from common.constant import HEADERS, USERNAME_ALREADY_EXISTS, USER_CREATED
from model.user import save_user


class SignUp(Resource):

    @classmethod
    def get(cls):
        return make_response(render_template('signup.html'), HEADERS)

    @classmethod
    def post(cls):
        username = request.form.get('username')
        email = request.form.get('email')
        try:
            save_user(username, email)
            return make_response(render_template('signup.html', message=USER_CREATED.format(username)), HEADERS)

        except DuplicateKeyError:
            return make_response(render_template('signup.html', message=USERNAME_ALREADY_EXISTS.format(username)),
                                 HEADERS)
