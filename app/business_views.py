from app import app, db, login_manager
import flask
from datetime import datetime
from .models import User, Review, Business

@app.route('trends/')
def trends():
    
