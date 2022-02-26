from app import server, db
from app.models.DataLoad import DataLoad
from app.models.Scrapped import Scrapped
from app.utils.to_dict import object_as_dict
from flask import render_template, request, redirect, url_for, session
from app.utils.preprocessing import case_folding, lang_detect, stopword_title, stemmed
import pandas as pd
from app.utils.apriori_calculate import call_calc

@server.route("/calculate")
def calculate():
  total_data = db.session.query(Scrapped, DataLoad).filter(DataLoad.id == Scrapped.data_load_id).order_by(Scrapped.id.desc()).count()
  db.session.close()
  return render_template("calculate.html",total_data=total_data, title="Calculate")

@server.route("/calculate/process", methods=["GET", "POST"])
def calculate_process():
  if (request.method == 'POST'):
    support = float(request.form['support']) / 100
    print(support)
    confidence = float(request.form['confidence']) / 100
    outputFilter = int(request.form['outputFilter'])

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

    new_data  = []
    for d in stemmed_data:
      data_set_new = []
      for dn in list(d["title"].split(" ")):
        data_set_new.append(dn)
      new_data.append(data_set_new)
    
    data_result = call_calc(new_data,support,confidence, outputFilter)
    # print(data_result)
    if data_result == False:
      data_result = []
      # session['data_result'] = data_result
      return render_template("calculate-result.html", data_result=data_result)
      # return redirect(url_for("calculate_result"))
    else:
      # session['data_result'] = data_result
      db.session.close()
      if len(data_result) > 1000:
        data_result = data_result[:1000]
      return render_template("calculate-result.html", data_result=data_result)
      # return redirect(url_for("calculate_result"))

@server.route("/calculate/result")
def calculate_result():
  data_result = session.get('data_result', None)
  return render_template("calculate-result.html", data_result=data_result, title="Calculate")
