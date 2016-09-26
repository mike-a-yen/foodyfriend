from . import db
from datetime import datetime

db.create_all()

class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(80, nullable=False))
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True)
    
    def __init__(self, name, email, password, confirmed, admin=False, confirmed_on=None):
        self.name = name
        self.email = email
        self.password = password
        self.registered_on = datetime.utcnow()
        self.admin = admin
        self.confirmed = confirmed
        self.confirmed_on = confirmed_on


    def get_id(self):
        return self.email

    def is_confirmed(self):
        return self.confirmed
    
    def __repr__(self):
        return '<Name %r>' % self.name
