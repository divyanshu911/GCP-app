import logging
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'fuck  you bitch'

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occured')
    return 'An internal  error', 500