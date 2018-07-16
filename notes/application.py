from flask import Flask, render_template, request, session
from flask_session import Session
import os

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
# app.config["SECRET_KEY"] = os.urandom(16)
# print(app.config["SECRET_KEY"])

Session(app)

@app.route("/", methods=["GET", "POST"])
def index():
    if session.get("notes") is None:
        print("Notes not in session")
        session["notes"] = []
    else:
        print("Notes IS IN SESSION")
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)
   
    return render_template("index.html", notes=session["notes"])