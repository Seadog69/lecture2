# application.py

from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

title = "My Mad WebPage"

@app.route("/")
def index():
    my_headline = "Hello, You Crazy Crazy Mad Mad Mad World!!!"
    return render_template("index.html", title=title, headline=my_headline)

@app.route("/bye")
def bye():
    headline = "Goodbye you Coding Genius you"
    return render_template("index.html", title=title, headline=headline)

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    headline = str.format(f"Hello you Coding SAVANT GENIUS, {name}")
    return render_template("index.html", title=title, headline=headline, name=name)