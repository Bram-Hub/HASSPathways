from flask import Flask, render_template
import pathlib

app = Flask(__name__)

@app.route("/")
def homepage():
	return render_template('temp.html')

if __name__ == "__main__":
	 app.run()