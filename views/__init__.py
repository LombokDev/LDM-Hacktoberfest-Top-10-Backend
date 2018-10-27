from flask import Blueprint, request, jsonify
from boot import socketio
import random
import json
import config

base = Blueprint('base', __name__)


@base.route('/')
def index():
    return 'Hello Flask!'

@base.route('/broadcast-top10', methods=['POST'])
def broadcast():
    data = request.get_json(True)
    socketio.emit('top-ten', data)
    return jsonify({'status': 'event broadcasted!'})