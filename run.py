from flask import Flask
from app import create_app

http_server = create_app(Flask)

if __name__ == "__main__":
    import os
    os.environ['FLASK_ENV'] = 'development'
    http_server.run('0.0.0.0', debug=True, port=5000)
