""" chat application """
from flask import Flask
from flask_socketio import SocketIO, join_room, leave_room
from flask_restful import Api
from flask_login import LoginManager
from dotenv import load_dotenv

from model.date_message import check_date, save_date
from model.message import save_message
from model.room_members import check_user_in_room, create_room_members
from model.user import get_user
from resources.login import LoginPage
from resources.logout import LogOut
from resources.home import Home
from resources.signup import SignUp
from resources.room import ViewRoom
from resources.create_room import CreateRoom
from resources.join_room import JoinRoom
from services.authenticate import authenticated_only
from services.back_up_message import load_message
from services.check_image import check_image, compress_image
from common.routes import LOGIN, HOMEPAGE, LOGOUT, SIGNUP, ROOMS, CREATE_ROOM, JOIN_ROOM
from services.date_time import get_date, get_time
from services.store_file import store_file

app = Flask(__name__)
api = Api(app)
load_dotenv(".env", verbose=True)
app.config.from_object('default_config')
socketio = SocketIO(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login_page'


@login_manager.user_loader
def load_user(username):
    return get_user(username)


@socketio.on('join_room')
def handle_join_room_event(data):
    join_room(data['room'])
    socketio.emit('join_room_announcement', data, room=data['room'])


@socketio.on('send_message')
@authenticated_only
def handle_send_message_event(data):
    if check_user_in_room(data['room'], data['username']) is None:
        create_room_members(data['room'], data['username'])

    if check_date(get_date(), data['room']) is None:
        save_date(get_date(), data['room'])
    save_message(data['message'], data['username'], data['room'], get_date(), get_time())
    socketio.emit('receive_message', data, room=data['room'])


@socketio.on('leave_room')
def handle_leave_room(data):
    leave_room(data['room'])
    socketio.emit('leave_room_announcement', data, room=data['room'])


@socketio.on('load_backup')
@authenticated_only
def handle_load_backup(data):
    load_message(data)


@socketio.on('file_load')
@authenticated_only
def handle_file_load(data):
    if check_date(get_date(), data['room']) is None:
        save_date(get_date(), data['room'])
    save_message(data['name'], data['username'], data['room'], get_date(), get_time())
    if check_image(data['type']):
        data['binary'] = compress_image(data)
        socketio.emit('send_image_file', data)
    else:
        store_file(data)
        socketio.emit('send_file', data)


api.add_resource(LoginPage, LOGIN, endpoint="login_page")
api.add_resource(Home, HOMEPAGE, endpoint="home_page")
api.add_resource(LogOut, LOGOUT)
api.add_resource(SignUp, SIGNUP, endpoint="signup")
api.add_resource(ViewRoom, ROOMS, endpoint="room")
api.add_resource(CreateRoom, CREATE_ROOM, endpoint="create_room")
api.add_resource(JoinRoom, JOIN_ROOM, endpoint="join_room")

if __name__ == "__main__":
    socketio.run(app=app, debug=True)
