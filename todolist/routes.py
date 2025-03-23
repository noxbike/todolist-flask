from todolist import app
from flask import render_template, url_for
from todolist.forms import Login_form, Register_form, Todolist_form
@app.route('/')
def todolist_page():
    form = Todolist_form()
    return render_template('todolist.html', form = form)

@app.route('/register')
def register_page():
    form = Register_form()
    return render_template('register.html', form = form)

@app.route('/login')
def login_page():
    form = Login_form()
    return render_template('login.html', form = form)

@app.route('/parameter')
def parameter_page():
    return render_template('parameter.html')