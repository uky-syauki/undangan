from flask import render_template, url_for
from app import app

@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html", title="Home", user="Ahmad Syauki")


@app.route('/index2')
def index2():
	return render_template('index2.html')