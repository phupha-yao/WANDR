import os
from flask import Flask
#from flask_ngrok import run_with_ngrok 
from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.sql import func
#from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from flask_login import LoginManager
from datetime import datetime

ROOMS = ['A101','A102','A103','A104','A105','A106','A107','A108','A109','A110',
         'A201','A202','A203','A204','A205','A206','A207','A208','A209','A220']

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "swanisacutiepatootie"

# run_with_ngrok(app)

db = SQLAlchemy(app)
login_manager = LoginManager(app)

from cpabooking import routes


