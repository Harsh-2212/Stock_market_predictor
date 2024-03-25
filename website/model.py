from . import db
from flask_login import UserMixin
from sqlalchemy import DateTime, func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150))
    notes = db.relationship('Note')

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(DateTime(timezone=True),default=func.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))