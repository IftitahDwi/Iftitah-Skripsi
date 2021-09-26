from app import server, db
from app.models.DataLoad import DataLoad
from flask import render_template, request, redirect, url_for

@server.route("/load-data")
def load_data():
  data_load = DataLoad.query.all()
  return render_template("load_data.html", title="Table", data_load=data_load)

@server.route('/load-data/add', methods=['POST', 'GET'])
def create_load_data():
  if request.method == 'POST':
    nidn = request.form['nidn']
    niy = request.form['niy']
    load_name = request.form['load_name']
    gs_id = request.form['gs_id']
    request_data = DataLoad(nidn=nidn, niy=niy, load_name=load_name, gs_id=gs_id)
    db.session.add(request_data)
    db.session.commit()
  return redirect(url_for('load_data'))

@server.route('/load-data/delete/<id>')
def destroy_load_data(id):
  data_load_id = DataLoad.query.filter_by(id=id).first()
  db.session.delete(data_load_id)
  db.session.commit()
  return redirect(url_for('load_data'))

@server.route('/load-data/edit', methods=['POST', 'GET'])
def update_load_data():
  if request.method == 'POST':
    nidn = request.form['nidn']
    niy = request.form['niy']
    load_name = request.form['load_name']
    gs_id = request.form['gs_id']
    id = request.form['data_id']
    data_load = DataLoad.query.filter_by(id=int(id)).first()
    data_load.nidn = nidn
    data_load.niy = niy
    data_load.load_name = load_name
    data_load.gs_id = gs_id
    db.session.commit()
    # request_data = DataLoad(nidn=nidn, niy=niy, load_name=load_name, gs_id=gs_id)
    # db.session.add(request_data)
    # db.session.commit()
  return redirect(url_for('load_data'))