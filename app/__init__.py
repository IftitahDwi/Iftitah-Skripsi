from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

server = Flask(__name__)
server.debug = True
server.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///system.db"
db = SQLAlchemy(server)
migrate = Migrate(server, db)

from app.views import Home
from app.views import Load_Data
# from app import views
