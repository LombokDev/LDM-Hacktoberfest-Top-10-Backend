from flask import Flask
from flask_socketio import SocketIO

import loader

app = Flask(__name__)
socketio = SocketIO(app)
app.config.from_object('config')

loader.load(app)
