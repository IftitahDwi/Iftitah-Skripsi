from app import server
from flask import render_template

@server.route("/")
def index():
  people = {
    "name":"hendi",
    "age":24,
    "address": "Pati, Jateng"
  }
  peoples = ["alvin", "arif", "bima"]
  return render_template("index.html", peoples=peoples)