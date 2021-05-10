from flask_login import UserMixin
from . import mysql

class User(UserMixin, mysql.Model):
    id = mysql.Column(mysql.Integer, primary_key=True)
    email = mysql.Column(mysql.String(100), unique=True)
    password = mysql.Column(mysql.String(21))
    username = mysql.Column(mysql.String(21))
    isActive = mysql.Column(mysql.Integer)