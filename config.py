import os

basedir = os.path.abspath(os.path.dirname(__name__)) # __name__ means "this files name"


class Config():
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')