from app import server, db
from flask import render_template

@server.route("/load-data")
def load_data():
  return render_template("load_data.html", title="Table")