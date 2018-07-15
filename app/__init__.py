import os

from flask import Flask
from flask_login import LoginManager

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config, TestConfig

app = Flask(__name__)

if os.environ.get('FLASK_ENV') == 'Testing':
    app.config.from_object(TestConfig)
else:
    app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'auth.login'

from app.auth import bp as auth_bp
from app.menu import bp as menu_bp
from app.order_counter import bp as order_counter_bp

app.register_blueprint(auth_bp, url_prefix='/')
app.register_blueprint(menu_bp, url_prefix='/menu')
app.register_blueprint(order_counter_bp, url_prefix='/order_counter')

from app import models
