#!/usr/bin/python3
from flask import Flask
from flask_restx import Api
from app.api import create_api


def create_app():
    app = Flask(__name__)

    app.register_blueprint(create_api())

    return app
