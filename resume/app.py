#!flask/bin/python
from flask import Flask,current_app, render_template
from flask_cors import CORS

app = Flask(__name__, template_folder='./template', static_folder='./static')
CORS(app)




with app.app_context():
    # within this block, current_app points to app.
    print current_app.name


@app.route('/')
def index():

    return render_template('index.html')

app.run(host='0.0.0.0', port=5000)