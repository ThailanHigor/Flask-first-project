from flask import Flask, request
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"

def create_app(enviroment):
    app = Flask(__name__)
    app.config.from_object(config[enviroment])

    db.init_app(app)
    login_manager.init_app(app)

    from app import routes
    routes.load(app)

    @app.template_filter("upper")
    def upper_filter(text):
        return text.upper()

    return app
