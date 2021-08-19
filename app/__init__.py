from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

server = Flask(__name__)
server.debug = True
server.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///jaya.db"
db = SQLAlchemy(server)
migrate = Migrate(server, db)

from app import views