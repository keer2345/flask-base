import os
from flask import Flask
from flask_wtf import CsrfProtect
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from config import config

basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()
csrf = CsrfProtect()

# Set up Flask-Login
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'account.login'


def create_app(config_enviroment):
    app = Flask(__name__)

    app.config.from_object(config[config_enviroment])

    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # not using sqlalchemy event system, hence disabling it

    config[config_enviroment].init_app(app)

    # Create app blueprints
    from app.main import main_bp
    app.register_blueprint(main_bp)

    from app.account import account_bp
    app.register_blueprint(account_bp, url_prefix='/account')

    return app
