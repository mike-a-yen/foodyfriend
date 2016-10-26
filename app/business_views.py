from app import app, db, login_manager
from app.utils import (get_states, get_cities,
                       validate_city, validate_state,
                       remove_None_from_dict)
import flask
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import mpld3
from wordcloud import WordCloud, STOPWORDS
from .models import User, Review, Business, Category


@app.route('/clouds')
def clouds():
    bids = db.session.query(Business.business_id,
                            Business.name)\
                            .filter(Category.category=='Pizza')\
                            .all()
    idx = np.random.randint(0, len(bids))
    bid, name = bids[idx]
    print('*'*50)
    print(name,bid)
    print('*'*50)
    query = db.session.query(Review.text,
                             Review.stars).filter_by(business_id=bid)
    reviews = pd.DataFrame(query.all())
    body = reviews['text'].str.cat().lower()
    wc = WordCloud(stopwords=STOPWORDS,
                   max_words=3000,
                   margin=10,
                   background_color='black',
                   random_state=1).generate(body)
    cloud_file = 'app/static/img/'+name+'.png'
    wc.to_file(cloud_file)
    return flask.render_template('cloud.html',
                                 cloud=name+'.png')
    
    
@app.route('/trends',methods=['GET','POST'])
def trends():
    data = {}
    if flask.request.method == 'POST':
        data['current_state'] = flask.request.form.get('state')
        data['current_city'] = flask.request.form.get('city')
        print('#'*70)
        print(flask.request.form.get('city'))
        print(data['current_city'])
        print('#'*70)
    data['states'] = get_states(city=data.get('current_city'))
    data['cities'] = get_cities(state=data.get('current_state'))
    filters = remove_None_from_dict({'city':data.get('current_city',None),
                                     'state':data.get('current_state',None)})
    if filters != {}:
        query = db.session.query(Business.name,
                                 Business.city,
                                 Business.state,
                                 Business.review_count,
                                 Business.stars).\
                filter(Category.category=='Pizza').\
                filter(Category.business_id==Business.business_id).\
                filter_by(**filters)
        print('*'*100)
        print(filters)
        print(query.all())
        print('*'*100)
        data['fields'] = query.first().keys()
        data['table'] = [dict(zip(row.keys(),row)) for row in query.all()]
        
        
    if data.get('current_city') and not validate_city(data.get('current_city')):
        flask.flash('Not a valid city','error')
        return flask.redirect('trends')
    if data.get('current_state') and not validate_state(data.get('current_state')):
        flask.flash('Not a valid state','error')
        return flask.redirect('trends')
    print(data.get('cities'))
    return flask.render_template('trends.html',
                                 cities=data.get('cities'),
                                 states=data.get('states'),
                                 current_city=data.get('current_city'),
                                 current_state=data.get('current_state'),
                                 fields=data.get('fields'),
                                 table=data.get('table'))
