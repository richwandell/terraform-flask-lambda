from flask_migrate import Migrate
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .app import create_app

app = create_app(Flask)
db = SQLAlchemy()
migrate = Migrate(app, db)