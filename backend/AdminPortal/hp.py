from flask import Flask, render_template, redirect, url_for, request, Blueprint, abort
import pathlib
import os
import json
import html

app = Flask(__name__)

#reading the courses json file
with open('./data/courses.json', 'r') as course_file:
    course_data = course_file.read()

with open('./data/pathways.json', 'r') as pw_file:
    pw_data = pw_file.read()

@app.route("/")
def homepage():
	#dis is getting mad at me
	return render_template("homepage.html", title="page", jsonfile_course=json.dumps(course_data),jsonfile_pw=json.dumps(pw_data) )

@app.route("/STSH", methods=['GET', 'POST'])
def STSH():
	#figure out a way 
	if(request.method == 'POST'):
		return render_template("courseList1.html")

if __name__ == "__main__":
	 app.run(host='localhost', debug=True)