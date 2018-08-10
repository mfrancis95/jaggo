from datetime import date
from flask import Flask, render_template
from os import environ

_record_end = date.fromordinal(int(environ['RECORD_END']))
_record_start = date.fromordinal(int(environ['RECORD_START']))
_record = (_record_end - _record_start).days
_start_date = date.fromordinal(int(environ['START_DATE']))

app = Flask(__name__)

@app.route('/')
def index():
    today = date.today()
    days = (today - _start_date).days
    global _record
    if days >= _record:
        _record = days
        global _record_end
        _record_end = today
        global _record_start
        _record_start = _start_date
    return render_template('index.html', record = _record, record_end = _record_end, record_start = _record_start, text = environ['TEXT'].format(days, 'day' if days == 1 else 'days'))