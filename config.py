import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'secretKEY'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL'] = "postgresql://postgres:42gdk2480t@localhost:5432/books_store"

class ProductionConfig(Config):
    DEBUG = False
class StagingConfig(Config):
    DEVELOPMENT=True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True