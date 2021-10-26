from app import server, db
from app.models.DataLoad import DataLoad
from app.models.Scrapped import Scrapped
from app.utils.to_dict import object_as_dict
from flask import render_template, request, redirect, url_for
from app.utils.preprocessing import case_folding, lang_detect, stopword_title, stemmed
import pandas as pd

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
  
  case_folding_data = case_folding(scrapped)
  lang_detect_data = lang_detect(case_folding_data)
  stopword_data = stopword_title(lang_detect_data)
  stemmed_data = stemmed(stopword_data)

  new_data_set=[]
  for data in stemmed_data:
      for new_data in data["title"].split(" "):
          data_result = {
          "name": data["name"],
          "gs_id": data["gs_id"],
          "title": new_data, "year": data["year"]}
          new_data_set.append(data_result)

  db.session.close()
  return render_template("preprocessing.html",result_datas = new_data_set)