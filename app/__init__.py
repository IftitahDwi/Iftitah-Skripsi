from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

server = Flask(__name__)
server.debug = True
server.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///jaya.db"
db = SQLAlchemy(server)
migrate = Migrate(server, db)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username= db.Column(db.String(80), unique=True, nullable=False)
  email= db.Column(db.String(200), unique=True, nullable=False)

  def __repr__(self):
    return "<User %r>" % self.username

from app import views