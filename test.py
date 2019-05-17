from flask import Flask

app = Flask(__name__)

from app import routes

app.route('/')
def tester():
    return '<h1>HELLO</h1>'