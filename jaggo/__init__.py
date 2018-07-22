from datetime import date
from flask import Flask, render_template
from os import environ

_start_date = date.fromordinal(int(environ['START_DATE']))

app = Flask(__name__)

@app.route('/')
def index():
    days = (date.today() - _start_date).days
    return render_template('index.html', text = environ['TEXT'].format(days, 'day' if days == 1 else 'days'))