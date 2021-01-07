from flask import Flask

app = Flask(__name__)


@app.route('/')
def say_hello():
    response_data = {
        "Status": 200,
        "Message": "Up and Running",
        "Developed By": "Ashutosh Krishna"
    }
    return response_data, 200


if __name__ == "__main__":
    app.run(debug=True)
