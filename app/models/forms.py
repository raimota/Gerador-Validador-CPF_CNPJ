from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class Campos(FlaskForm):
    es = StringField('es')