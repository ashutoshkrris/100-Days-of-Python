from flask import Flask, render_template
from datetime import datetime
import requests


def guess_age(name):
    response = requests.get(f"https://api.agify.io?name={name}")
    return response.json()["age"]


def guess_gender(name):
    response = requests.get(f"https://api.genderize.io?name={name}")
    return response.json()["gender"]


current_year = datetime.now().year

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html", current_year=current_year)


@app.route('/guess/<string:name>')
def guess(name):
    age = guess_age(name)
    gender = guess_gender(name)
    return render_template("result.html", age=age, gender=gender.capitalize(), name=name, current_year=current_year)


if __name__ == '__main__':
    app.run(debug=True)
