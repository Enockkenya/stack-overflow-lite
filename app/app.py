from flask_api import FlaskAPI
from flask import request, jsonify, abort

# local import
from Instance.config import app_config

def create_app(config_name):

    app = FlaskAPI(__name__, instance_relative_config=True)
    
    users = []
    questions = []
    answers = []


 
                

    @app.route('/api/v1/questions', methods=['POST'])
    def question():
        # Post a question
        question = {'id': len(questions)+1,
            'Questions': request.json.get('Question'),
            'Date posted': request.json.get('Date posted')
        }
        questions.append(question)
        return jsonify({'Message': "Question successfully created"} ,{'Questions': questions}), 201




    return app