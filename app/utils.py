import json

def load_json(fname):
    with open(fname,'r') as f:
        return json.load(f)
