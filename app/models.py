from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db, login
from flask_login import UserMixin


class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))
#	status = db.Column(db.String(10), default="admin")
	terjual = db.relationship('Terjual', backref="author", lazy='dynamic')
	def set_password(self, password):
		self.password_hash = generate_password_hash(password)
	def check_password(self, password):
		return check_password_hash(self.password_hash, password)
	def __repr__(self):
		return '<User {}>'.format(self.username)



class Barang(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	kode_barang = db.Column(db.String(15), unique=True)
	nama_barang = db.Column(db.String(30))
	harga_jual = db.Column(db.Integer)
	harga_modal = db.Column(db.Integer)
	tersedia = db.Column(db.Integer)
	def __repr__(self):
		return '<Barang {}>'.format(self.kode_barang)



class Terjual(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	timestamp = db.Column(db.DateTime, index=True, default=datetime.now)
#	kode_toko = db.Column(db.String(15))
	kode_barang = db.Column(db.String(15))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	def __repr__(self):
		return '<Terjual {}>'.format(self.kode_barang)

