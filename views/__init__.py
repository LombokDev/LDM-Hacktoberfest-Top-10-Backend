from flask import Blueprint

base = Blueprint('base', __name__)


@base.route('/')
def index():
    return 'Hello Flask!'
