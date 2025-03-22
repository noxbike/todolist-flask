from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app  = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todolist.db'
db = SQLAlchemy(app)

from todolist import routes
