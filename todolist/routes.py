from todolist import app, db
from flask import render_template, url_for, flash, get_flashed_messages, redirect, request
from todolist.forms import Login_form, Register_form, Todolist_form
from todolist.models import User, Todos
from flask_login import login_user, logout_user, login_required, current_user
@app.route('/', methods=['GET','POST'])
@login_required
def todolist_page():
    form = Todolist_form()
    todos = Todos.query.filter_by(owner=current_user.id)
    if form.validate_on_submit():
        new_task = Todos(title=form.title.data, description=form.description.data, owner=current_user.id)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('todolist_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'{err_msg}', category='danger')
    return render_template('todolist.html', form = form, todos = todos)

@app.route('/register', methods=['GET','POST'])
def register_page():
    form = Register_form()
    if form.validate_on_submit():
        new_user = User(name = form.name.data, email=form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login_page'))
    if form.errors != {}:
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

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Todos.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return redirect(url_for('todolist_page'))
    
@app.route('/completion/<int:task_id>', methods=['GET'])
def toggle_completion(task_id):
    task = Todos.query.get(task_id)
    if(task):
        task.completed = not task.completed
        db.session.commit()
    return redirect(url_for('todolist_page'))

@app.route('/edit/<int:task_id>', methods=['GET','POST'])
def edit_task(task_id):
    print(task_id)
    task =Todos.query.get(task_id)
    if(task):
        task.title = request.form['title']
        task.description = request.form['description']
        db.session.commit()
    return redirect(url_for('todolist_page'))