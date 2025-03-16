#!/usr/bin/python3
from flask import Flask
from flask_restx import Api
from app.api import create_api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from config import DevelopmentConfig

bcrypt = Bcrypt()
jwt = JWTManager()

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)

    app.config.from_object(config_class)

    app.register_blueprint(create_api())

    bcrypt.init_app(app)

    jwt.init_app(app)

    return app
