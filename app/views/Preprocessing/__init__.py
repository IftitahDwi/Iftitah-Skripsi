from app import server, db
from app.models.DataLoad import DataLoad
from app.models.Scrapped import Scrapped
from app.utils.to_dict import object_as_dict
from flask import render_template, request, redirect, url_for

@server.route("/preprocessing")
def preprocessing():
  join_data = db.session.query(Scrapped, DataLoad).filter(DataLoad.id == Scrapped.data_load_id).order_by(Scrapped.id.desc())
  scrapped = []
  for s, l in join_data:
    scrapped_data = {
      "id": s.id,
      "name": l.load_name,
      "title": s.title,
      "year": s.year,
      "gs_id": l.gs_id
    }
    scrapped.append(scrapped_data)

  db.session.close()
  return render_template("preprocessing.html")