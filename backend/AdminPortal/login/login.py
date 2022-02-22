from flask import Flask, render_template, redirect, url_for, request, Blueprint
from flask_login import LoginManager
import pathlib

app = Flask(__name__, template_folder=str(pathlib.Path(__file__).parent.absolute()))

login = LoginManager()
login.init_app(app)

@login.user_loader
def load(user):
	return User.get(user)

@app.route("/")
def dashboard():
	'''
	if(user is logged in):
		redirect to dash
	else
		redirect to login
	'''

@app.route("/login", methods = ['GET', 'POST'])
def login():
	if request.method == 'POST':
		user = request.form.get('user')
		passwrd = request.form.get('passwrd')

		return str('USERNAME IS: ' + user + 'PASSWORD IS: ' + passwrd)
	else:
		return render_template("login.html")

if __name__ == "__main__":
	app.run()
