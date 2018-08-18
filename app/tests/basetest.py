"""base class for all the tests"""
from unittest import TestCase
import unittest
from app.app import app

class BaseTestCase(TestCase):

    """ set up configurations for the test environment"""
    @classmethod
    def setUpClass(self):
        """set up app configuration"""
        self.app = app.test_client()
        self.app.testing = True
        self.users = [
            {
                "user_id":1,
                "username": "enock",
                "email": "sean@gmail.com",
                "password": "sean123"
            },
            {
                "user_id":2,
                "username": "eno",
                "email": "sean28@gmail.com",
                "password": "sean123"
            },
         ]


        #user base  
        self.person = {
            "username": "sean",
            "email":"sean@gmail.com",
            "password": "sean123"
        }
        self.person_no_username = {
            "email": "sean@gmail.com",
            "password": "sean123"
        }
        self.person_no_email = {
            "username": "sean",
            "password": "sean123"
        }
        self.person_no_password = {
            "username": "sean",
            "email": "sean@gmail.com",
        }
        self.person_invalid_email = {
            "username": "sean",
            "email": "seee.com",
            "password": "sean123"
        }
        self.person_existing_user = {
            "username": "test",
            "email": "test@gmail.com",
            "password": "password"
        }
        self.correct_login = {
            "username": "sean",
            "password": "sean123"
            }
        self.wrong_login = {
            "username": "sean",
            "password": "sean"
            }
        self.no_username = {
            "username": "",
            "password": "sean123"
            }
        self.no_password = {
            "username": "sean",
            "password": ""
            }
        self.admin = {
            "username": "admin",
            "email": "admin@gmail.com",
            "password": "admin1234"
        }
        self.admin_correct = {
            "username": "admin",
            "password": "admn1234"
            }
        self.admin_wrong = {
            "username": "sean",
             "password": "mimi"
             }


    #question base
        self.question = {
            "question_id": 1,
            "user_id":1,
            "category":"how are you doing?",
            "body": "fogort hammer",
            "date_created": 21/5/18,
            "answers":0,
        }
        self.questions = [
            {
                "question_id": 1,
                "user_id":1,
                "category": "how are you doing?",
                "body": "fogort hammer",
                "date_created": 18/8/18,
                "answers":0,
            },
            {
                "question_id": 2,
                "user_id":1,
                "category": "how are you doing?",
                "body": "fogort hammer",
                "date_created": 15/5/18,
                "answers":0,
            },
           

            {
                "question_id": 3,
                "user_id":2,
                "category": "how are you doing?",
                "body": "fogort hammer",
                "date_created": 1/3/18,
                "answers":0,
            },
            {
                "question_id": 1,
                "user_id":1,
                "category": "how are you doing?",
                "body": "fogort hammer",
                "date_created": 21/3/18,
                "answers":0,
            }
        ]
        self.question_no_category = {
            "question_id": 1,
            "user_id":1,
            "category": "",
            "body": "fogort hammer",
            "date_created": 1/5/18,,
            "answers":0,
        }
        self.question_no_body = {
            "question_id": 1,
            "user_id":1,
            "category": "how are you doing?",
            "body": "",
            "date_created": 1/7/18,
            "answers":0,
        }
        self.question_invalid_category = {
            "question_id": 1,
            "user_id":1,
            "category": 1234,
            "body": "How come it 1234",
            "date_created": 11/3/18,
            "answers":0,
        }

       #answer base
        self.answer = {
            "answer_id": 1,
            "user_id":1,
            "question_id":2,
            "body": "baby i am lost",
            "date_created": 15//18,
            "upvotes":3,
            "downvotes":1,
            "answers":0,
        }
        self.answers = [
            {
                "answer_id": 1,
                "user_id":1,
                "question_id":2,
                "body": "i wish i knew",
                "date_created": 11/3/18,
                "upvotes":3,
                "downvotes":1,
    
            },
            {
                "answer_id": 2,
                "user_id":1,
                "question_id":2,
                "body": "nobody knows",
                "date_created": 18/4/18,
                "upvotes":3,
                "downvotes":1,
            
            },
            {
                "answer_id": 3,
                "user_id":1,
                "question_id":2,
                "body": "things are better",
                "date_created": 11/4/18,
                "upvotes":3,
                "downvotes":1,
               
            }
        ]
        self.answer_no_body = {
            "answer_id": 3,
            "user_id":1,
            "question_id":2,
            "body": "",
            "date_created": 1/7/18,
            "upvotes":3,
            "downvotes":1,
          
        }
       
if __name__ == '__main__':
    unittest.main()