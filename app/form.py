from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField
from wtforms.validators import InputRequired

class formDate(FlaskForm):
    date = DateField('Select a Date', validators=[InputRequired()], format="%Y-%m-%d")
    