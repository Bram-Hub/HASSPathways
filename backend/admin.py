# from crypt import methods
# from unicodedata import name
from flask import Flask, request, json, jsonify, session, redirect, url_for, render_template
from flask_cors import CORS, cross_origin
from cas import CASClient
import flask
from sqlalchemy import *
from FAQs.FAQ_Class import Faqs
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

flask.__version__
app = Flask(__name__)
c = CORS(app)
CORS(app, resources={r'/*': {'origins': '*'}}, CORS_SUPPORTS_CREDENTIALS=True)
app.config['CORS_HEADERS'] = 'Content-Type'

cas = CASClient(
    version=3,
    service_url='https://ec2-52-90-250-109.compute-1.amazonaws.com/login/rpi',
    server_url='https://cas.auth.rpi.edu/cas/'
)


@app.route('/', methods=['GET', 'POST'])
def default():
    return '''<h1> DEFAULT ADMIN PAGE </h1>'''


@app.route('/faqs', methods=['GET', 'POST'])
def load_faqs():
    path = 'FAQs/'
    file = path + 'faqs.json'
    with open(file) as json_file:
        faqs = json.load(json_file)
    return faqs


@app.route('/guard')
def guard(method=['GET']):
    if 'username' in session:
        return jsonify('{"auth": "1"}')
    else:
        return jsonify('{"auth": "0"}')


@app.route('/admin')
def index():
    return redirect(url_for('login'))


@app.route('/login/rpi', methods=["POST", "GET"])
def login():
    # print(next)
    ticket = request.args.get('ticket')
    if not ticket:
        print(cas.get_login_url())
        return redirect(cas.get_login_url())

    print(ticket)
    user, attributes, pgtiou = cas.verify_ticket(ticket)

    if not user:
        return "Failed to Verify Login Ticket"
    else:
        session['username'] = user
        return redirect("https://hasspathways.com/admin-portal")


@app.route("/edit", methods=["POST", "GET"])
def editAdmin():
    response = {'status': 'success'}
    if request.method == "POST":
        dat = request.get_json()
        name = dat.get('courses'),
        pathways = dat.get('pathways')
        print(name)
        print(pathways)

        response['message'] = 'Success!'

    return jsonify(response)


# @app.route('/test', methods=["GET"])
# def test():
#     return render_template("admin.html")


def updateFAQs():
    """
    Update all asked questions into the database.
    """
    path = 'FAQs/'
    file = path + 'faqs.json'
    with open(file) as json_file:
        faqs = json.load(json_file)
        db_engine = create_engine("sqlite:///faqs.db?check_same_thread=False")
        Base = declarative_base()
        Base.metadata.create_all(db_engine, checkfirst=True)
        Session = sessionmaker(bind=db_engine)
        FAQs_session = Session()
        FAQs_session.add_all([Faqs(Question=q, Answer=a) for q, a in faqs])
        FAQs_session.commit()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # http://127.0.0.1:5000/