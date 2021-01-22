from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/blog')
def blog():
   response = requests.get("https://technik-backend.herokuapp.com/api/blog/posts")
   all_posts = response.json()
   return render_template("blog.html", posts=all_posts[::-1])


if __name__ == '__main__':
    app.run(debug=True)
