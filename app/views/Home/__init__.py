from app import server, db
from app.models import DataLoad
from flask import render_template

@server.route("/")
def index():

  return render_template("index.html", title="Home")