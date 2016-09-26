from app import app
import flask
from datetime import datetime

@app.route('/')
def hello():
    now = datetime.utcnow().isoformat()
    return 'Hello World!<br>{}'.format(now)

@app.route('/login',methods=['GET','POST'])
def login():
    print(db)
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.get(form.email.data)
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True)
                return redirect(url_for("/"))
    return render_template("login.html", form=form)
