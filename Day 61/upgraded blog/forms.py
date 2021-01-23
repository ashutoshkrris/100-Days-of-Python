from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField('Email Address', validators=[
                        DataRequired(message="Email is required.")])
    password = PasswordField('Password', validators=[
                           DataRequired(message="Password is required.")])
    submit = SubmitField('Log In')
