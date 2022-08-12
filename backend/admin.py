from flask import Flask, request, json, jsonify
from flask_cors import CORS, cross_origin
app = Flask(__name__)
c = CORS(app)
CORS(app, resources={r'/*': {'origins': '*'}},CORS_SUPPORTS_CREDENTIALS = True)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/edit", methods=["POST", "GET"])
def editAdmin():
	response = {'status':'success'}
	if request.method == "POST":
		dat = request.get_json()
		name = dat.get('courses'),
		pathways = dat.get('pathways')
		print(name)
		print(pathways)

		response['message'] = 'Success!'

	return jsonify(response)

if __name__ == '__main__':
	app.run(debug=True)
