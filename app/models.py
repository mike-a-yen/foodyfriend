from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'
    __hash__ = 'pbkdf2:sha256:1000'
    id = db.Column('user_id',db.Integer, primary_key=True)
    email = db.Column('email',db.String(120), unique=True)
    password = db.Column('password',db.String(120))
    registered_on = db.Column('registered_on',db.DateTime)
    name = db.Column('name',db.String(120))
    
    def __init__(self, email, password, name=''):
        self.email = email
        self.password = generate_password_hash(password,method=self.__hash__)
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

    def check_password(self,password):
        return check_password_hash(self.password, password)
    
    def __repr__(self):
        return '<User %r - est. %s>' % (self.email,self.registered_on.isoformat())
    
class Review(db.Model):
    __tablename__ = 'reviews'
    
    id = db.Column('id',db.Integer, primary_key=True)
    funny = db.Column('funny',db.Integer)
    useful = db.Column('useful',db.Integer)
    cool = db.Column('cool',db.Integer)
    user_id = db.Column('user_id',db.String(80))
    review_id = db.Column('review_id',db.String(80))
    stars = db.Column('stars',db.Integer)
    date = db.Column('date',db.DateTime)
    text = db.Column('text',db.Text)
    type = db.Column('type',db.String(80))
    business_id = db.Column('business_id',db.ForeignKey('business.business_id'))
    
    def __init__(self, votes, user_id, review_id, stars, date, text, type, business_id):
        self.funny = votes.get('funny',0)
        self.useful = votes.get('useful',0)
        self.cool = votes.get('cool',0)
        self.user_id = user_id
        self.review_id = review_id
        self.stars = stars
        self.date = date
        self.text = text
        self.type = type
        self.business_id = business_id


class Business(db.Model):
    __tablename__ = 'business'

    id = db.Column('id',db.Integer, primary_key=True)
    business_id = db.Column('business_id',db.String(80))
    full_address = db.Column('full_address', db.String(120))
    #TODO: hours = db.Column() Mon-Sun
    open = db.Column('open', db.Boolean)
    city = db.Column('city', db.String(80))
    state = db.Column('state',db.String(80))
    name = db.Column('name', db.String(80))
    stars = db.Column('stars',db.Float)
    review_count = db.Column('review_count', db.Integer)
    #TODO: neighborhoods = db.Column()
    lon = db.Column('lon',db.Float)
    lat = db.Column('lat',db.Float)
    #TODO ambience
    price_range = db.Column('price_range', db.Integer)
    type = db.Column('type', db.String(80))
    
    def __init__(self, business_id, full_address, open, city, state, name,
                 stars, review_count, longitude, latitude, price_range, type):

        self.business_id = business_id 
        self.full_address = full_address
        self.open = open
        self.city = city
        self.state = state
        self.name = name
        self.stars = stars
        self.review_count = review_count
        self.lon = longitude
        self.lat = latitude
        self.price_range = price_range
        self.type = type



class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column('id',db.Integer, primary_key=True)
    business_id = db.Column('business_id',db.String(80),db.ForeignKey('business.business_id'))
    category = db.Column('category', db.String(80))
    
    def __init__(self, business_id, category):

        self.business_id = business_id 
        self.category = category

class Attribute(db.Model):
    __tablename__ = 'attribute'

    id = db.Column('id',db.Integer, primary_key=True)
    business_id = db.Column('business_id',db.String(80),db.ForeignKey('business.business_id'))
    noise_level = db.Column('noise_level', db.String(80))
    good_for_groups = db.Column('good_for_groups', db.Boolean)
    delivery = db.Column('delivery', db.Boolean)
    caters = db.Column('caters', db.Boolean)
    alcohol = db.Column('alcohol', db.String(80))
    reservations = db.Column('reservations', db.Boolean)
    outdoor = db.Column('outdoor', db.Boolean)
    credit_cards = db.Column('credit_cards', db.Boolean)
    takeout = db.Column('takeout', db.Boolean)
    tv = db.Column('tv', db.Boolean)
    drivethru = db.Column('drivethru', db.Boolean)
    attire = db.Column('attire', db.String(80))
    good_for_kids = db.Column('good_for_kids', db.Boolean)
    waiter = db.Column('waiter', db.Boolean)
    
    
    def __init__(self, business_id, noise_level, good_for_groups, delivery,
                 caters, alcohol, reservations, outdoor, credit_cards, takeout,
                 tv, drivethru, attire, good_for_kids, waiter):
        
        self.business_id = business_id 
        self.noise_level = noise_level 
        self.good_for_groups = good_for_groups
        self.delivery = delivery
        self.caters = caters
        self.alcohol = alcohol
        self.reservations = reservations
        self.outdoor = outdoor
        self.credit_cards = credit_cards
        self.takeout = takeout
        self.tv = tv
        self.drivethru = drivethru 
        self.attire = attire
        self.good_for_kids = good_for_kids
        self.waiter = waiter

class Feature(db.Model):
    __tablename__ = 'feature'

    id = db.Column('id',db.Integer, primary_key=True)
    business_id = db.Column('business_id',db.String(80),db.ForeignKey('business.business_id'))
    phrase = db.Column('phrase', db.String(120))
    pos = db.Column('pos', db.String(12))
    positive = db.Column('positive',db.Integer)
    count = db.Column('count',db.Integer)
    def __init__(self, business_id, phrase, pos, positive, count):
        
        self.business_id = business_id 
        self.phrase = phrase
        self.pos = pos
        self.positive = positive
        self.count = count

        
print('Creating DB')
db.create_all()
