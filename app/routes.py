from flask import render_template, url_for, redirect
from app import app
from app.form import formDate
from app.dbHandle import DataBase

@app.route('/')
@app.route('/index')
def index():
	allData = DataBase()
	x = allData.bulan
	y = allData.cariUntukTahun("2023")
	form = formDate()
	if form.validate_on_submit():
		if form.tahun.data == True:
			tahun = form.date.data.split('-')
			x = allData.bulan
			y = allData.cariUntukTahun(tahun[0])
		if form.bulan.data == True:
			bulan = form.date.data.split('-')
			x = allData.tanggal
			y = allData.cariUntukBulan(bulan[0]+"-"+bulan[1])
	return render_template("index.html", title="Home", user="Ahmad Syauki",x=x,y=y,form=form)


@app.route('/index2')
def index2():
	return render_template('index2.html')