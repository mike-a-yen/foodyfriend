from flask import Flask

app = Flask(__name__)

from app import views, utils

settings = utils.load_json('config/config.json')
