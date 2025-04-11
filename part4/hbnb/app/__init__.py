#!/usr/bin/python3
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig
import os

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app(config_class=DevelopmentConfig):
    static_path = os.path.join(os.path.dirname(__file__), 'frontend', 'static')

    app = Flask(
        __name__,
        static_folder=static_path,
        static_url_path='/static'
    )
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from app.api import create_api
    app.register_blueprint(create_api())

    from app.frontend import create_frontend
    app.register_blueprint(create_frontend())

    return app
