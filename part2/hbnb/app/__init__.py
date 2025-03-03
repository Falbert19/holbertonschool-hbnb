#!/usr/bin/python3
from flask import Flask
from flask_restx import Api
from app.api import create_api


def create_app():
    app = Flask(__name__)
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API')

    app.register_blueprint(create_api())

    return app
