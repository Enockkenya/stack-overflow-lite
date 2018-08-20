from flask_api import FlaskAPI
from flask import request, jsonify, abort

# local import
from Instance.config import app_config

def create_app(config_name):

    app = FlaskAPI(__name__, instance_relative_config=True)


    return app