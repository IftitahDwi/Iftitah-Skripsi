from app import server, db
from app.models.DataLoad import DataLoad
from flask import render_template

@server.route("/load-data")
def load_data():
  data_load = DataLoad.query.all()
  return render_template("load_data.html", title="Table", data_load=data_load)