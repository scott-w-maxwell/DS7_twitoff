"""SQLalchemy models for twitoff"""

from flask-sqlalchemy import SQLALchemy
from .models import DB


DB = SQLalchemy()

class User(DB.Model):
    """Twitter users that we pull and analyze"""
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(15), nullable = False)

class Tweet(DB.Model):
    """Tweet"""
    id = DB.Column(DB.Integer, primary_key=True)
    text = DB.Column(DB.Unicode(280))