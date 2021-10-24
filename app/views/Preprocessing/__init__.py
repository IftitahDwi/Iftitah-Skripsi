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
  
  # print(scrapped)
  print("####this result case folding start")
  case_folding_data = case_folding(scrapped)
  print(len(case_folding_data))
  print("####this result case folding end")

  print("####this result lang detect start")
  lang_detect_data = lang_detect(case_folding_data)
  print(len(lang_detect_data))
  print("####this result lang detect end")

  print("####this result stopword title start")
  stopword_data = stopword_title(lang_detect_data)
  print(len(stopword_data))
  print("####this result stopword title end")

  print("####this result stemming title start")
  stemmed_data = stemmed(stopword_data)
  print(stemmed_data)
  print("####this result stemming title end")
  # df_data = pd.DataFrame(stemmed_data)
  # print(df_data)
  new_data_set=[]
  for data in stemmed_data:
      for new_data in data["title"].split(" "):
          data_result = {
          "name": data["name"],
          "gs_id": data["gs_id"],
          "title": new_data, "year": data["year"]}
          new_data_set.append(data_result)
    # print(scrapped.)
  # print(lang_detect(case_folding(titles)))

  db.session.close()
  return render_template("preprocessing.html",result_datas = new_data_set)