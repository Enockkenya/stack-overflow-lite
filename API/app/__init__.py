""" initialize the app """
from flask import Flask 
from api.config import CONFIG
from api.Questions.views import Questions
from api.Answers.views import Answers
from flask_restful import Api

def create_app():
    app=Flask(__name__)
    
    return app

app = Flask(__name__)

api = Api(app)
app.config.from_pyfile('config.py')


