import os, redis


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = 'redis'
    SESSION_PERMANENT = False
    SESSION_REDIS = redis.from_url(os.environ.get('SESSION_REDIS'))


class LocalConfig(BaseConfig):
    DEBUG = True
