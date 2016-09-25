from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
import os
from app import views, utils
from app.config import settings

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)
