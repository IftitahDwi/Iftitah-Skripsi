from flask import Flask
# from flask_script import Manager
from flask_migrate import Migrate
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

server = Flask(__name__)
server.debug = True
server.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///system.db"
from app.models import db

migrate = Migrate(server, db)

# app = Manager(server)
# app.add_command('db', MigrateCommand)
# db = SQLAlchemy(server)

from app.views import Home
from app.views import Load_Data
# from app import views
