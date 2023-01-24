"""
A webapp framework in python , module api contains a flask app with a single endpoint.
instance of flask app is WSGI application
name - application module or package 
/ - defining our route to trigger our function
Default content type in HTML
python Interpretor :conda used 
Execution : set FLASK_APP=app.py and  set FLASK_ENV=development, flask run 
will run on loalhost:5000
"""
from flask import Flask
from flask import request
import logging


logging.basicConfig(filename='debug.log',level=logging.DEBUG ,format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def hello_world():
    if request.method == 'GET':
        return get_method()
    else :
        return post_method()
@app.get('/')
def get_method():
    if request.headers['Accept'] == 'application/json' :
        return {"message": "Hello, World"}
    if len(request.headers['Accept']) == 0:
        return "<p>Hello, World</p>"
@app.post('/')
def post_method():
    return " POST METHOD"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)