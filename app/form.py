from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, BooleanField, SubmitField, RadioField
from wtforms.validators import InputRequired

class formDate(FlaskForm):
    date = DateField('Tanggal', validators=[InputRequired()], format="%Y-%m-%d")
    radioTahun = RadioField("Berdasarkan",choices=[('tahun','Tahun'),('bulan',"Bulan")])
    submit = SubmitField("Tampilkan")
    