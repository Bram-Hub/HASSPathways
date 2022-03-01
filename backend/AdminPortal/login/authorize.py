from flask import Flask, flash, render_template, request
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
	authkey = db.Column(db.String(16), unique = True)


@app.route("/", methods = ['GET','POST'])
def register():
	if request.method == 'POST':
		

		name = request.form.get('name')
		email = request.form.get('email')
		passwrd = request.form.get('passwrd')
		authkey = request.form.get('authkey')
		print(name)
		print(email)
		print(passwrd)

		newUser = User(username=email, passwrd=hashPass(passwrd), name=name, authkey=authkey)
 
		db.session.add(newUser)
		db.session.commit()

		return "Great Job!"
		
	else:
		return render_template('signup.html')

if __name__ == "__main__":
	app.run(debug=True);




