#!/usr/bin/python3
from flask import Blueprint
from flask_restx import Api

from app.api.v1.users import api as users_ns

api_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(api_v1, title='HBNB API', version='1.0', description='HBNB API v1')

api.add_namespace(users_ns, path='/users')
