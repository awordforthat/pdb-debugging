import json


def load_data(limit=200):
    raw = json.loads(open("jeopardy.json", "r").read())
    return raw[:limit]
