from app import server, db
from app.models import User
from flask import render_template

@server.route("/")
def index():
  ###create data
  req_user = User(username="jos", email="jos@gg.com")
  db.session.add(req_user)
  db.session.commit()
  print("data sudah masuk")

  ###delete data
  # del_user = User.query.filter_by(id="3").delete()
 
  # del_users.commit()
  print("haha sudah delete")


  ### update data
  # admin = User.query.filter_by(username='admin').first()
  # admin.email = 'my_new_email@example.com'
  # db.session.commit()

  # user = User.query.get(2)
  # user.username = 'mas robi jos'
  # db.session.commit()
  
  ###get all data
  user = User.query.all()
  # people = {
  #   "name":"hendi",
  #   "age":24,
  #   "address": "Pati, Jateng"
  # }
  # peoples = ["alvin", "arif", "bima"]
  return render_template("index.html", peoples=user)