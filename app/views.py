from app import app, db, login_manager
import flask
from flask_login import login_user, login_required
import flask_login
from datetime import datetime
from .models import User, Recipes, Ingredients

@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html', user={'email':'john'})

@app.route('/users')
def users():
    table = User.query.all()
    print(table)
    return flask.render_template("table.html", table=table)

@app.route('/register',methods=['GET','POST'])
def register():
    if flask.request.method == 'GET':
        return flask.render_template('register.html')
    user = User(flask.request.form['email'],
                flask.request.form['password'])
    print(user)
    db.session.add(user)
    db.session.commit()
    flask.flash('Registration Successfully Completed!')
    return flask.redirect('/login')

@app.route('/login',methods=['GET','POST'])
def login():
    if flask.request.method == 'GET':
        return flask.render_template('login.html')
    email = flask.request.form['email']
    password = flask.request.form['password']
    registered_user = User.query.filter_by(email=email,password=password).first()
    if registered_user == None:
        flask.flash('email or password invalid', 'error')
        return flask.redirect('/login')
    login_user(registered_user)
    flask.flash('Logged in successfully')
    return flask.redirect(flask.request.args.get('next') or flask.url_for('index'))

@app.route('/profile')
@login_required
def profile():
    user = flask_login.current_user
    print(user)
    return flask.render_template('profile.html', current_user=user)

@app.route('/edit_profile',methods=['GET','POST'])
@login_required
def edit_profile():
    current_user = flask_login.current_user
    print(current_user.id)
    print(current_user.email)
    print(current_user.name)
    if flask.request.method == 'GET':
        return flask.render_template('edit_profile.html',current_user=current_user)
    email = flask.request.form.get('email',current_user.email)
    password = flask.request.form.get('password',current_user.password)
    name = flask.request.form.get('name',current_user.name)

    user = User.query.filter_by(id=current_user.id).first()
    user.name = name
    user.email = email
    user.password = password
    db.session.commit()
    return flask.redirect(flask.request.args.get('next') or flask.url_for('profile'))
    

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
