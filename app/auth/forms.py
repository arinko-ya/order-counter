from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_again = PasswordField(
        'Password Again', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


class PasswordChangeForm(FlaskForm):
    current_password = PasswordField(
        'Current Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired()])
    new_password_again = PasswordField(
        'New Password Again',
        validators=[DataRequired(), EqualTo('new_passsword')])
    submit = SubmitField('Password Change')
