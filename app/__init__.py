from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view= 'login'

#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/mayen/Programming/foodyfriend/tmp/yelp.db'
app.config['SECRET_KEY'] = 'secret'
db = SQLAlchemy(app)

from app import utils, user_views, business_views
