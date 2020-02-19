from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app.secret_key = "auddie"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///artbox.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
ACCESS_KEY =  'AKIA5T5I5DCPVAHBS57A'
SECRET_KEY = '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'
S3_LOCATION = 'http://{}.s3.amazonaws.com/'.format('kidsartbox')
bcrypt = Bcrypt(app)
db = SQLAlchemy(app) 
migrate = Migrate(app, db)


