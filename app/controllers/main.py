from flask import render_template
from app import app
from app.models.forms import Campos

@app.route('/')
def index():
    form = Campos()
    return render_template('index.html',form=form)
