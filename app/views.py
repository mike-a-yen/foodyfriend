from app import app
import time

@app.route('/')
def hello():
    now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    return 'Hello World!<br>{}'.format(now)
