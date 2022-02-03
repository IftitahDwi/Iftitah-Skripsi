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

  #filter and insert early title to prepocessing title
  source_data = []
  for source in scrapped:
    for result in lang_detect_data:
      if source["id"] == result["id"]:
        new_data = {
          "id": result["id"],
          "name": result["name"],
          "s_title": source["title"],
          "title": result["title"],
          "year": result["year"],
          "gs_id": result["gs_id"]
        }
        source_data.append(new_data)

  stopword_data = stopword_title(source_data)
  stemmed_data = stemmed(stopword_data)
  print("this is final")

  db.session.close()
  return render_template("preprocessing.html",result_datas = stemmed_data, title="Preprocessing")