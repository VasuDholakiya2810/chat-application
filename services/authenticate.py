""" Authenticate Decorator """
import functools

from flask import redirect, url_for
from flask_login import current_user
from flask_socketio import disconnect


def authenticated_only(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        if current_user.is_authenticated:
            return f(*args, **kwargs)
        else:
            disconnect()
            return redirect(url_for('login_page'))
    return wrapped

