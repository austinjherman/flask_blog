from flask_wtf import Form
from wtforms import validators, StringField, PasswordField
from wtforms.fields.html5 import EmailField


class RegisterForm(Form):
    fullname = StringField('Full name', [validators.Required()])
    email    = EmailField('Email', [validators.Required()])
    username = StringField('Username', [
        validators.Required(),
        validators.Length(min=4, max=25)
        ])
    password = PasswordField('Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Your passwords do not match.'),
        validators.Length(min=4, max=80)
        ])
    confirm  = PasswordField('Confirm password')
