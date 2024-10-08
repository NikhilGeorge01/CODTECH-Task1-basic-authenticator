from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
lm = LoginManager()
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, "auth.db")
app.config['SECRET_KEY'] = 'this-is-my-secret'
db = SQLAlchemy(app)
lm.init_app(app)
lm.session_protection = "strong"
lm.login_view = "login"
from .views import *
from .models import *
