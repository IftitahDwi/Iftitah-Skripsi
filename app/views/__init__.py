from app import server, db
from app.models import User
from flask import render_template

@server.route("/")
def index():
  return render_template("index.html", title="Home")

@server.route("/table")
def table():
  return render_template("table.html", title="Table")