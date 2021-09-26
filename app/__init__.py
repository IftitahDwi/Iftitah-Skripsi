from flask import Flask
from flask_migrate import Migrate

server = Flask(__name__)
server.debug = True
server.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///system.db"

from app.models import db

migrate = Migrate(server, db)

from app.views import Home
from app.views import Load_Data
