from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db.db'
app.config["SECRET_KEY"]='12345678'
db = SQLAlchemy(app)
login = LoginManager(app)
from nera import routes


