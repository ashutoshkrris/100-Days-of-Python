from flask import Flask, render_template
from post import posts

all_posts = posts()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/post/<string:slug>')
def single_post(slug):
    requested_post = None
    for post in all_posts:
        if post["slug"] == slug:
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
