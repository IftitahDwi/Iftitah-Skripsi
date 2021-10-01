from app import server, db
from app.models.DataLoad import DataLoad
from flask import render_template, request, redirect, url_for

@server.route("/data-scrapped", methods=["GET","POST"])
def data_scrapped():
  data_load = DataLoad.query.order_by(DataLoad.id.desc())
  return render_template("data_scrapped.html", title="Scrapped Data")