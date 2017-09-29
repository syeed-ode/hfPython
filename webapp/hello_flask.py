"""Module for building a basic web application running the Flask web server

Available Functions:
    - hello(): Uses the Flask route decorator to process request on the '/' path on port 5000

"""
from flask import Flask
from vsearch_local import search4letters

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    """Base method from root path to proves everything works out ok"""
    return "Hello World from Flask!"


@app.route('/search4')
def do_search() -> str:
    """Esecutes a created script with defaulted text"""
    return str(search4letters('life, the universe, and everything in between'))


app.run()