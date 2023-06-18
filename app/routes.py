from flask import render_template, url_for
from app import app
from app.form import formDate
from app.dbHandle import DB

@app.route('/')
@app.route('/index')
def index():
	allData = DB()
	x = allData.data.forStatYearKey
	y = allData.data.forStatYearValue
	form = formDate()
	if form.validate_on_submit():
		pilihan = form.date.data
	return render_template("index.html", title="Home", user="Ahmad Syauki",x=x,y=y)


@app.route('/index2')
def index2():
	return render_template('index2.html')