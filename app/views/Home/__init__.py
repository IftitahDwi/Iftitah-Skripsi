from app import server, db
from app.models.DataLoad import DataLoad
from flask import render_template

@server.route("/")
def index():
  print(DataLoad.query.all())
  return render_template("index.html", title="Home")