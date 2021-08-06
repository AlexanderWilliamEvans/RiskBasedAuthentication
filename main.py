import flask
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>POC: Risk based authentication</h1><hr/><p>This site is a prototype API risk based authentication " \
           "novels.</p> "


@app.route('/risk/verifyUser', methods=['GET'])
def verify_user():
    client = request.args.get('client')
    username = request.args.get('username')
    password = request.args.get('password')


app.run()
