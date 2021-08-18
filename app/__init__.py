from flask import Flask
server = Flask(__name__)
server.debug = True

from app import views