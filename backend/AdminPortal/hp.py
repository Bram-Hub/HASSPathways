from flask import Flask, render_template, redirect, url_for, request, Blueprint, abort
import pathlib
import os
import json
import html

app = Flask(__name__)

@app.route("/")
def homepage():
	#dis is getting mad at me
	return render_template('homepage.html')

@app.route("/STSH", methods=['GET', 'POST'])
def STSH():
	#figure out a way 
	if(request.method == 'POST'):
		return render_template("courseList1.html")

if __name__ == "__main__":
	 app.run()
