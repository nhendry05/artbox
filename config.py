from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.secret_key = "auddie"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///artbox.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
bcrypt = Bcrypt(app)
db = SQLAlchemy(app) 
migrate = Migrate(app, db)

