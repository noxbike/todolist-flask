from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

class Register_form(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()], render_kw={"class":'form-control', 'placeholder':'Enter your email'})
    name = StringField('Name', validators=[DataRequired()], render_kw={"class":'form-control', 'placeholder':'Enter your name'})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"class":'form-control', 'placeholder':'Enter your password'})
    password2 = PasswordField('Confirm your password', validators=[DataRequired(), EqualTo('password', message="Passwords must match!")], render_kw={"class":'form-control', 'placeholder':'Enter your password again'})
    submit = SubmitField('Register',render_kw={"class":' btn btn-primary'})

class Login_form(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()], render_kw={"class":'form-control', 'placeholder':'Enter your email'})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"class":'form-control', 'placeholder':'Enter your password'})
    submit = SubmitField('Login',render_kw={"class":' btn btn-primary'})

class Todolist_form(FlaskForm):
    title = StringField('Title', validators=[DataRequired()], render_kw={"class":'form-control', 'placeholder':'Task title'})
    description = StringField('Description', validators=[DataRequired()], render_kw={"class":'form-control', 'placeholder':'Task description'})
    submit = SubmitField('Add Task',render_kw={"class":' btn btn-primary'})