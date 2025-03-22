from todolist import app
from flask import render_template, url_for
@app.route('/')
def todolist_page():
    return render_template('todolist.html')

@app.route('/register')
def register_page():
    return render_template('register.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/parameter')
def parameter_page():
    return render_template('parameter.html')