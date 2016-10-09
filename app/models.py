from . import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column('user_id',db.Integer, primary_key=True)
    email = db.Column('email',db.String(120), unique=True)
    password = db.Column('password',db.String(120))
    registered_on = db.Column('registered_on',db.DateTime)
    name = db.Column('name',db.String(120))
    
    def __init__(self, email, password, name=''):
        self.email = email
        self.password = password
        self.registered_on = datetime.utcnow()
        self.name = name
        
    def get_id(self):
        return self.id

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def __repr__(self):
        return '<User %r - est. %s>' % (self.email,self.registered_on.isoformat())
    
class Recipes(db.Model):
    __tablename__ = 'recipes'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
        
    def __init__(self, name):
        self.name = name


class Ingredients(db.Model):
    __tablename__ = 'ingredients'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
        
    def __init__(self, name):
        self.name = name

class RecipeIngredients(db.Model):
    __tablename__ = 'recipe_ingredients'

    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column('recipe_id',db.Integer)
    ingredient_id = db.Column('ingredient_id',db.Integer)
    amount = db.Column('amount',db.Float)
    units = db.column('units',db.String(80))

    def __init__(self, recipe_id, ingredient_id, amount, units):
        self.recipe_id = recipe_id
        self.ingredient_id = ingredient_id
        self.amount = amount
        self.units = units



print('Creating DB')
db.create_all()
