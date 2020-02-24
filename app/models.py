from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

database = SQLAlchemy()

from .api.models import *
from .auth.models import *

db = database
