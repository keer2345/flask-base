import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import config

basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()


def create_app(config_enviroment):
    app = Flask(__name__)

    app.config.from_object(config[config_enviroment])

    db.init_app(app)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # not using sqlalchemy event system, hence disabling it

    config[config_enviroment].init_app(app)

    return app
