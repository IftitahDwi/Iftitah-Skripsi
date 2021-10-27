from app import server, db
from app.models.DataLoad import DataLoad
from app.models.Scrapped import Scrapped
from flask import render_template, session

@server.route("/")
def index():
  load_data_count = DataLoad.query.count()
  scraped_data = db.session.query(Scrapped, DataLoad).filter(DataLoad.id == Scrapped.data_load_id).order_by(Scrapped.id.desc()).count()
  data_result = session.get('data_result', None)
  return render_template("index.html", title="Home", load_data_count=load_data_count, scraped_data=scraped_data, data_result=data_result)