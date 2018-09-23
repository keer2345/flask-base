import os

from flask import Flask
from flask_assets import Environment
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CsrfProtect

from app.assets import app_css, app_js, vendor_css, vendor_js
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

    # Register Jinja template functions
    from .utils import register_template_utils
    register_template_utils(app)

    # Set up asset pipeline
    assets_env = Environment(app)

    dirs = ['assets/styles', 'assets/scripts']
    for path in dirs:
        assets_env.append_path(os.path.join(basedir, path))
    assets_env.url_expire = True

    assets_env.register('app_css', app_css)
    assets_env.register('app_js', app_js)
    assets_env.register('vendor_css', vendor_css)
    assets_env.register('vendor_js', vendor_js)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # not using sqlalchemy event system, hence disabling it

    config[config_enviroment].init_app(app)

    # Create app blueprints
    from app.main import main_bp
    app.register_blueprint(main_bp)

    from app.account import account_bp
    app.register_blueprint(account_bp, url_prefix='/account')

    return app
