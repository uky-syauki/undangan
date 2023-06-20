from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, BooleanField, SubmitField, RadioField
from wtforms.validators import InputRequired

class formDate(FlaskForm):
    date = DateField('Tanggal', validators=[InputRequired()], format="%Y-%m-%d")
    radioTahun = RadioField("Berdasarkan",choices=[(True,'Tahun')])
    radioBulan = RadioField("Berdasarkan",choices=[(True,"Bulan")])
    submit = SubmitField("Tampilkan")
    