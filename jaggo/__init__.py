from flask import Flask, render_template, request
from datetime import date
from os import environ

_start_date = date.fromordinal(int(environ['START_DATE']))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', days = (date.today() - _start_date).days, text = environ['TEXT'])