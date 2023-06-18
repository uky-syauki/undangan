from flask import render_template, url_for
from app import app
from app.form import formDate
from app.dbHandle import DataBase

@app.route('/')
@app.route('/index')
def index():
	allData = DataBase()
	x = allData.forStatYearKey
	y = allData.forStatYearValue
	form = formDate()
	if form.validate_on_submit():
		pilihan = form.date.data
	return render_template("index.html", title="Home", user="Ahmad Syauki",x=x,y=y)


@app.route('/index2')
def index2():
	return render_template('index2.html')