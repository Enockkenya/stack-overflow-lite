import unittest
import os
import json

from app.app import create_app
from app.models import Question, Answer

class StackOverflow_lite(unittest.TestCase):
    """ Answers model."""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.questions = {'Question': 'who is the best coder in the world', 'Date posted': '12/3/2018'}
        self.answers = {'Answer': 'seve jobs?? mark facebook??', 'Date posted': '12/3/2018'}


    # def test_post_question(self):
    #     """Testing posting a question."""
    #     response = self.client.post(
    #         '/api/v1/questions/1/answers', data=json.dumps(self.questions), content_type='application/json')
    #     self.assertEqual(response.status_code, 201)
    #     data = json.loads(response.get_data())
    #     self.assertEqual(data[0]['Message'], "Question successfully created")
