from todolist import db, bcrypt,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    todos = db.relationship('Todos', backref='user', lazy=True)

    @property
    def password(self):
        return self.password
    @password.setter
    def password(self, attempted_password):
        self.password_hash = bcrypt.generate_password_hash(attempted_password).decode('utf-8')
    
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

class Todos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)