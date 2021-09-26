from app import server, db
from app.models.DataLoad import DataLoad
from flask import render_template

@server.route("/")
def index():
  load_data_count = DataLoad.query.count()
  return render_template("index.html", title="Home", load_data_count=load_data_count)