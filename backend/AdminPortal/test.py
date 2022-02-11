from flask import Flask, render_template, redirect, url_for, request, Blueprint
from test2 import test2
import pathlib

app = Flask(__name__, template_folder=str(pathlib.Path(__file__).parent.absolute()))

app.register_blueprint(test2)


@app.route("/")
def dashboard():
	return render_template("login.html")

@app.route("/login")
def login():
	return "Logged in!"

if __name__ == "__main__":
	app.run()
