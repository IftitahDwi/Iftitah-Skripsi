from app import server, db
from app.models.DataLoad import DataLoad
from app.models.Scrapped import Scrapped
from flask import render_template, request, redirect, url_for
import json
from ast import literal_eval

@server.route("/data-scrapped", methods=["GET","POST"])
def data_scrapped():
  data_loads = DataLoad.query.all()
  print(type(data_loads))
  def object_as_dict(obj):
    return {c.key: getattr(obj, c.key) for c in db.inspect(obj).mapper.column_attrs}
  print(data_loads)
  # # decode =  [dict(r) for r in data_loads]
  # # print(decode)
  # for d in data_loads:
  print([object_as_dict(i) for i in data_loads])

  return render_template("data_scrapped.html", title="Scrapped Data")