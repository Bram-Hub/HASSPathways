from flask import Flask, render_template, redirect, url_for, request, Blueprint, abort
import pathlib
import os
import json
import html

app = Flask(__name__)


#TODO: update path on server once you have it working
c = open('/data/courses.json','r')
p = open('/data/pathways.json','r')

coursesData = json.load(c)
pathwaysData = json.load(p)

#https request

@app.route("/")
def homepage():
	#dis is getting mad at me
	to_send=database()
	return render_template("homepage.html", title="page", to_send=to_send )

@app.route("/STSH", methods=['GET', 'POST'])
def STSH():
	#figure out a way 
	if(request.method == 'POST'):
		return render_template("courseList1.html")

if __name__ == "__main__":
	 app.run(host='localhost', debug=True)