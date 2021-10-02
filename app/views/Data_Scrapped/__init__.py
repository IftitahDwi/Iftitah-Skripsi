from app import server, db
from app.models.DataLoad import DataLoad
from app.models.Scrapped import Scrapped
from app.utils.to_dict import object_as_dict
from flask import render_template, request, redirect, url_for
from bs4 import BeautifulSoup
import httpx
import pandas as pd
import lxml

@server.route("/data-scrapped", methods=["GET","POST"])
async def data_scrapped():
  #get all data from data_load tables
  data_loads = DataLoad.query.filter_by(is_scraped=False).all()
  data_loads_dict = object_as_dict(data_loads)
  
  #start to scrapping with google scholar id
  client = httpx.AsyncClient()
  titles = []
  authors = []
  years = []
  id = []

  for index, data_load in enumerate(data_loads_dict):
      response = await client.get("https://scholar.google.com/citations?hl=id&user=" + data_load["gs_id"])
      soup = BeautifulSoup(response.content,"lxml")
      authorDom = soup.findAll("div", {"class": "gs_gray"})
      titles.append([i.text for i in soup.findAll("a", {"class": "gsc_a_at"})])
      # print(titles)
      authors.append([authorDom[idx].text for idx, i in enumerate(authorDom) if (idx+1)%2 == 1])
      # print(authors)
      years.append([i.text for i in soup.findAll("span", {"class": "gs_ibl"})])
      id.append([data_load["id"] for i in soup.findAll("a", {"class": "gsc_a_at"})])
      # print(years)
  await client.aclose()
  author_flats = [y for x in authors for y in x]
  title_flats = [y for x in titles for y in x]
  year_flats = [y for x in years for y in x]
  id_flats = [y for x in id for y in x]

  #parsing to dataframe
  df = pd.DataFrame({
    "scrapped_name":author_flats,"title":title_flats, "year":year_flats, "data_load_id": id_flats
  })
  #parsing to diect
  result = df.to_dict('records')
  #bulk insert into Scrapped database
  db.session.bulk_insert_mappings(Scrapped,result)
  db.session.commit()  
  for data in data_loads_dict:
    id = data["id"]
    data_load = DataLoad.query.filter_by(id=id).first()
    data_load.is_scraped = False
    db.session.commit()

  # df.to_sql("article", con=db, if_exists="replace")
  # print([object_as_dict(i) for i in data_loads])
  # for j in data_loads:
  #   object_j = {
  #     'nidn':j.nidn
  #   }
  #   print(object_j)

  return render_template("data_scrapped.html", title="Scrapped Data")