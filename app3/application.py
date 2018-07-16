# application.py

from flask import Flask, render_template

app = Flask(__name__)

title = "My Mad WebPage"

@app.route("/")
def index():
    headline = "Hello, You Crazy Crazy Mad Mad Mad World!!!"
    return render_template("index.html", title=title, headline=headline)

@app.route("/bye")
def bye():
    headline = "Goodbye you Coding Genius you"
    return render_template("index.html", title=title, headline=headline)

if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.run(debug=True)