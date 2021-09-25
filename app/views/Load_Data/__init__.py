from app import server, db
from app.models import User
from flask import render_template

@server.route("/load-data")
def load_data():
  return render_template("load_data.html", title="Table")