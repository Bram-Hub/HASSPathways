from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
	return render_template("login.html")

if __name__ == "__main__":
	app.run()