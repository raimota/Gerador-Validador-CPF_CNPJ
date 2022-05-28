from flask import Flask
from flask_script import Manager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

app.config.from_object('config')

manager = Manager(app)

from app.controllers import main
from app.models import forms
from app.templates import *