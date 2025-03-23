from todolist import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    todos = db.relationship('Todos', backref='user', lazy=True)

class Todos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    owner = db.Column(db.Integer, db.ForeignKey('user.idf'), nullable=False)