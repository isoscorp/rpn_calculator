from flask import Flask
from flask_restplus import Api

from model.base import Session

app = Flask("RPN")
api = Api(app)

session = Session()
