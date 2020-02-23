from flask_lambda import FlaskLambda
from app import create_app

app = create_app(FlaskLambda)
