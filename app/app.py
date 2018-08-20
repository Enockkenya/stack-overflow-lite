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

    @app.route('/api/v1/questions', methods=['GET'])
    def view_all_questions():
        # retrieve all questions
        return jsonify({'Questions': questions}), 200

    @app.route('/api/v1/questions/<int:id>', methods=['GET'])
    def single_question(id):
        # retrive a question by it's ID
        single_question = [question for question in questions if question['id'] == id]
        if len(single_question) == 0:
            return jsonify({'Message': "No question found"})

        return jsonify({'Questions': single_question}), 200


    return app