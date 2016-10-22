from app import app, db, login_manager
from app.utils import get_states, get_cities, validate_city, validate_state
import flask
from datetime import datetime
from .models import User, Review, Business, Category

@app.route('/trends',methods=['GET','POST'])
def trends():
    current_state = None
    current_city = None
    if flask.request.method == 'POST':
        current_state = flask.request.form.get('state')
        current_city = flask.request.form.get('city')
        
    states = get_states(city=current_city)
    cities = get_cities(state=current_state)
    
    if current_city and not validate_city(current_city):
        flask.flash('Not a valid city','error')
        return flask.redirect('trends')
    if current_state and not validate_state(current_state):
        flask.flash('Not a valid state','error')
        return flask.redirect('trends')
    
    return flask.render_template('trends.html',
                                 current_state=current_state,
                                 current_city=current_city,
                                 states=states,
                                 cities=cities)
