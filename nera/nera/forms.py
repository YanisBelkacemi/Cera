from email.policy import default
from tkinter import Label
from flask_wtf import FlaskForm
from wtforms import StringField , SubmitField , PasswordField , EmailField  , TextAreaField
from wtforms.validators import DataRequired



class posting(FlaskForm):

    text = TextAreaField(label="want say something :", validators=[DataRequired()])
    doit = SubmitField(label="post")

class register(FlaskForm):
    firstname = StringField(label="firstname : ", validators=[DataRequired()])
    familyname = StringField(label="familly name", validators=[DataRequired()])
    password = PasswordField(label="Password : ", validators=[DataRequired()])
    Email = EmailField(label="Email :   ", validators=[DataRequired()])
    register = SubmitField(label="Register")

class login(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired()])
    password = PasswordField(label="password", validators=[DataRequired()])
    submit = SubmitField(label="Login")

class adminf(FlaskForm):
    admin = StringField(label="admin")
    submit = SubmitField()

