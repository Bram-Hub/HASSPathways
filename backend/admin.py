# from crypt import methods
# from unicodedata import name
from flask import Flask, request, json, jsonify, session, redirect, url_for, render_template
from flask_cors import CORS, cross_origin
from cas import CASClient
import flask
from sqlalchemy import *
from sqlalchemy import MetaData
from FAQs.FAQ_Class import Faqs
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
    db_engine = create_engine("sqlite:///FAQs.db")
    Session = sessionmaker(bind=db_engine)
    FAQs_session = Session()
    all_questions = FAQs_session.query(Faqs).all()
    result = {}
    for q in all_questions:
        result[q.Question] = q.Answer
    FAQs_session.close()
    return result


@app.route('/addqa', methods=['GET'])
def addQA():
    return render_template('AddQA.html')


@app.route('/addqa', methods=['Post'])
def addQAResult():
    db_engine = create_engine("sqlite:///FAQs.db")
    Session = sessionmaker(bind=db_engine)
    FAQs_session = Session()
    res = FAQs_session.query(Faqs).filter_by(Question=request.form['question']).first()
    if not res:
        FAQs_session.add(Faqs(Question=request.form['question'], Answer=request.form['answer']))
        FAQs_session.commit()
        FAQs_session.close()
        return '''<h1> Question Added </h1>'''
    else:
        res.Answer = request.form['answer']
        FAQs_session.commit()
        FAQs_session.close()
        return '''<h1> Question in table, Answer Updated </h1>'''


@app.route('/deleteqa', methods=['Get'])
def deleteQA():
    db_engine = create_engine("sqlite:///FAQs.db")
    Session = sessionmaker(bind=db_engine)
    FAQs_session = Session()
    all_questions = FAQs_session.query(Faqs).all()
    result = {}
    for q in all_questions:
        result[q.Question] = q.Answer
    FAQs_session.close()
    return render_template('DeleteQA.html', faqs=result)


@app.route('/deleteqa', methods=['Post'])
def deleteQA_result():
    db_engine = create_engine("sqlite:///FAQs.db")
    Session = sessionmaker(bind=db_engine)
    FAQs_session = Session()
    # delete the selected questions
    for question in request.form.getlist("questions"):
        FAQs_session.query(Faqs).filter(Faqs.Question == question).delete()
        FAQs_session.commit()
    FAQs_session.close()
    return '''<h1>Question(s) deleted</h1>'''


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

def updateFAQsFromJson():
    """
    Update all asked questions into the database.
    """
    file = 'FAQs/faqs.json'
    with open(file) as json_file:
        faqs = json.load(json_file)

        # get to the table
        db_engine = create_engine("sqlite:///FAQs.db")

        # create table
        meta = MetaData()
        Questions = Table(
            'questions', meta,
            Column('Question', String, primary_key=True),
            Column('Answer', String)
        )
        meta.create_all(db_engine, checkfirst=True)

        # upload using sessionmanager
        Session = sessionmaker(bind=db_engine)
        FAQs_session = Session()
        data = []
        for q, a in faqs.items():
            if not FAQs_session.query(Faqs).filter_by(Question=q).first():
                data.append(Faqs(Question=q, Answer=a))
        FAQs_session.add_all(data)
        FAQs_session.commit()
        FAQs_session.close()


if __name__ == '__main__':
    # updateFAQsFromJson()
    app.run(host='0.0.0.0', port=5000, debug=True)  # http://127.0.0.1:5000/
