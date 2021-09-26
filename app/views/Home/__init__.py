from app import server, db
from flask import render_template

@server.route("/")
def index():
  return render_template("index.html", title="Home")