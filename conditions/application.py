import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1 # Boolean that is true if month and day are 1/1
    # For testing purposes
    new_year = True
    return render_template("index.html", new_year=new_year)