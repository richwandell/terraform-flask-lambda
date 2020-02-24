from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import database as db


class Account(db.Model):
    __tablename__ = "account"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Unicode)
    account_users = db.relationship('User')


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=True)
    last_name = db.Column(db.String, nullable=True)
    account = db.Column(db.Integer, db.ForeignKey('account.id'))
    username = db.Column(db.String, nullable=False, index=True, unique=True)
    password_hash = db.Column(db.String(158), nullable=False, index=True, unique=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password, method="pbkdf2:sha512")

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
