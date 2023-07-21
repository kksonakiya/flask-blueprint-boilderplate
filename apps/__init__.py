from importlib import import_module
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from apps import api, authentication, home

import sys, os
from config import Config
app = Flask(__name__, static_folder='static')
db = SQLAlchemy()
login_manager = LoginManager()



def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)


def initialize_dbmodels():
    from apps.authentication.models import Users

    return True


def configure_database(app):
    with app.app_context():
        initialize_dbmodels()
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()


def initialize_routes():
    from apps.api import routes
    from apps.authentication import routes
    from apps.home import routes

    return True


def register_blueprints(app):
    # initialize_routes()
    # app.register_blueprint(api.blueprint)
    # app.register_blueprint(authentication.blueprint)
    # app.register_blueprint(home.blueprint)
    for module_name in ('api', 'authentication', 'home'):
        module = import_module("apps.{}.routes".format(module_name))
        app.register_blueprint(module.blueprint)


def create_app(config=Config):
    app.config.from_object(config)
    register_extensions(app)
    configure_database(app)
    register_blueprints(app)
    return app
