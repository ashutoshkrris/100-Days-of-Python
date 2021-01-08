from flask import Flask
from datetime import datetime

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


@app.route('/')
def time_now():
    return f'{datetime.utcnow()}'


@app.route('/hello')
@make_bold
@make_emphasis
@make_underlined
def say_hello():
    return f'Hello'


if __name__ == "__main__":
    app.run(debug=True)
