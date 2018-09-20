import os
from config import config

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))


db = SQLAlchemy()


def create_app(config_enviroment):
    app = Flask(__name__)
    app.config.from_object(config[config_enviroment])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # not using sqlalchemy event system, hence disabling it
    
    config[config_enviroment].init_app(app)

    return app

