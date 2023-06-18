from flask import render_template, url_for
from app import app
from app.form import formDate
from app import DataBase


@app.route('/')
@app.route('/index')
def index():
	x = DataBase.forStatYearKey
	y = DataBase.forStatYearValue
	form = formDate()
	if form.validate_on_submit():
		pilihan = form.date.data
	return render_template("index.html", title="Home", user="Ahmad Syauki",x=x,y=y)


@app.route('/index2')
def index2():
	return render_template('index2.html')