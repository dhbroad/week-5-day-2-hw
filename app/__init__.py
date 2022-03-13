from flask import Flask
from config import Config

app = Flask(__name__) # instantiating the flask object. We also inherited a lot of methods and attributes

app.config.from_object(Config) # from_object is one of the things we inherited from flask

from . import routes # from "." ie "inside this folder", import routes to connect all the files together