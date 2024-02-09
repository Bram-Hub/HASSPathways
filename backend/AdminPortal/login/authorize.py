from flask import Flask, flash, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from passlib.context import CryptContext
from db import db

db = SQLAlchemy()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

def verify(password, Hash):
	return CryptContext(schemes=["bcrypt"], deprecated="auto").verify(password, Hash)

def hashPass(password):
	return CryptContext(schemes=["bcrypt"], deprecated="auto").hash(password)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(32), unique = True)
	passwrd = db.Column(db.String(64), unique = True)
	name = db.Column(db.String(64))
	authkey = db.Column(db.String(16))

@app.route("/register", methods = ['GET','POST'])
def register():
	if request.method == 'POST':
		
		name = request.form.get('name')
		email = request.form.get('email')
		passwrd = request.form.get('passwrd')
		authkey = request.form.get('authkey')

		print(name)
		print(email)
		print(passwrd)

		if(email == passwrd):
			return "Your email should not be the same as your password!"

		if User.query.filter_by(username=email).first():
			return "HELLL NA"
		elif name == email:
			return "Username should not be same as password!"


		newUser = User(username=email, passwrd=hashPass(passwrd), name=name, authkey=authkey)

 
		db.session.add(newUser)
		db.session.commit()

		return redirect(url_for("dashboard"))

	else:
		return render_template('signup.html')

@app.route("/login", methods = ['GET', 'POST'])
def dashboard():

	if(request.method == 'POST'):

		username = request.form.get("user")
		passwrd = request.form.get("passwrd")

		user = User.query.filter_by(username=username).first()

		if user != None and verify(passwrd, hashPass(passwrd)):
			return "Logged!"
		return "No!"
	else:
		return render_template('login.html')

if __name__ == "__main__":
	app.run(debug=True);




