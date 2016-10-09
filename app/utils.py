import json
from . import login_manager
from .models import User

def load_json(fname):
    with open(fname,'r') as f:
        return json.load(f)

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)
