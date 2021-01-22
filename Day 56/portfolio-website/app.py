from flask import Flask
from flask.templating import render_template

app = Flask(__name__)


@app.route('/test')
def test():
    data = {
        "Status": 200,
        "Message": "Up and Running"
    }
    return data

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
