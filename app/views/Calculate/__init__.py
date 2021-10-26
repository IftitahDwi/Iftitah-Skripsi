from app import server, db
from app.models.DataLoad import DataLoad
from app.models.Scrapped import Scrapped
from flask import render_template, request, redirect, url_for

@server.route("/calculate")
def calculate():
  total_data = db.session.query(Scrapped, DataLoad).filter(DataLoad.id == Scrapped.data_load_id).order_by(Scrapped.id.desc()).count()
  return render_template("calculate.html",total_data=total_data)

@server.route("/calculate/process", methods=["GET", "POST"])
def calculate_process():
  if (request.method == 'POST'):
    support = int(request.form['support'])
    confidence = int(request.form['confidence'])
  return
  # return render_template("calculate.html")
