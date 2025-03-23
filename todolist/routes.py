from todolist import app, db
from flask import render_template, url_for, flash, get_flashed_messages, redirect
from todolist.forms import Login_form, Register_form, Todolist_form
from todolist.models import User, Todos
from flask_login import login_user, logout_user, login_required
@app.route('/')
@login_required
def todolist_page():
    form = Todolist_form()
    return render_template('todolist.html', form = form)

@app.route('/register', methods=['GET','POST'])
def register_page():
    form = Register_form()
    if form.validate_on_submit():
        new_user = User(name = form.name.data, email=form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login_page'))
    if form.errors != {}:
        print(form.errors)
        for err_msg in form.errors.values():
            flash(f'there was and error! : {err_msg}', category='danger')
    return render_template('register.html', form = form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = Login_form()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(email = form.email.data).first()
        if attempted_user and attempted_user.check_password(password = form.password.data):
            login_user(attempted_user)
            return redirect(url_for('todolist_page'))
        else:
            flash('Email and password does not match! Please try again', category='danger')

    return render_template('login.html', form = form)

@app.route('/parameter')
@login_required
def parameter_page():
    return render_template('parameter.html')

@app.route('/logout')
def logout_page():
    logout_user()
    flash('you have logged out!', category = 'info')
    return redirect(url_for('login_page'))