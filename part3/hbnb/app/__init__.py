#!/usr/bin/python3
from flask import Flask
from flask_restx import Api
from app.api import create_api
from flask_bcrypt import Bcrypt


def create_app(config_class=config.DevelopmentConfig):
    app = Flask(__name__)

    app.config.from_object(config_class)

    app.register_blueprint(create_api())

    bcrypt.init_app(app)

    return app
