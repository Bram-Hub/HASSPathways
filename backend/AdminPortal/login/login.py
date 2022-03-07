from flask import Flask, render_template, redirect, url_for, request, Blueprint
from flask_login import LoginManager
from authorize import db, verify, User
import pathlib

app = Flask(__name__, template_folder=str(pathlib.Path(__file__).parent.absolute()))

login = LoginManager()
login.init_app(app)

@login.user_loader
def load(user):
	return User.get(user)

@app.route("/login", methods = ['GET', 'POST'])
def dashboard():

	if(request.method == 'POST'):
		username = request.form.get("user")
		passwrd = request.form.get("passwrd")

		user = User.query.filter_by(email=username).first()

		if user == None or authorize.verify(user.passwrd, hashPass(passwrd)):
			return "Logged!"
		return 
	else:
		return render_template('login.html')



	'''
	if(user is logged in):
		redirect to dash
	else
		redirect to login
	'''

#@app.route()

if __name__ == "__main__":
	app.run()
