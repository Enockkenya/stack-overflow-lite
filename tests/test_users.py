import unittest
import os
import json

from app.app import create_app
from app.models import User

class StackOverflow_lite_Users(unittest.TestCase):
    """This class represent Users."""

    def setUp(self):
        """Define test variables and initialize."""
        self.client = create_app(config_name="testing")
        self.client = self.client.test_client()
        self.user = {
            "username": "enock", "email": "enock@gmail.com", "password": "125"
            }
        self.user_no_username = {
            "email": "enock@gmail.com",
            "password": "125"
        }
        self.user_no_email = {
            "username": "enock",
            "password": "125"
        }
        self.user_no_password = {
            "username": "enock",
            "email": "enock@gmail.com",
        }
        self.user_invalid_email = {
            "username": "enock",
            "email": "enock.com",
            "password": "125"
        }
        self.user_existing = {
            "username": "test",
            "email": "test@gmail.com",
            "password": "password"
        }
        self.correct_login = {"username": "enock",
                              "password": "125"}
        self.wrong_login = {"username": "enock",
                            "password": "andela"}
        self.no_username = {"username": "",
                            "password": "125"}
        self.no_password = {"username": "enock",
                            "password": ""}
      

    def test_signup_user(self):
        """Test to register new user."""
        response = self.client.post(
            '/api/v1/auth/signup', data=json.dumps(self.user), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        dataman = json.loads(response.get_data())
        self.assertEqual(dataman['message'], 'User successfully registered!')
    

    def test_signin_user(self):
        """Test to login a registered user."""
        response = self.client.post(
            '/api/v1/auth/signin', data=json.dumps(self.user), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        
        
    # #     #no username
    #     response = self.client.post('/api/v1/auth/signup',
    #                              data=json.dumps(self.user_no_username), content_type = "application/json")
    #     self.assertEqual(response.status_code, 400)
    #     dataman = json.loads(response.get_data())
    #     self.assertEqual(dataman['message'], 'User successfully registered!')

    # #     #no email
    #     response = self.client.post('api/v1/auth/signup',
    #                              data=json.dumps(self.user_no_email),
    #                              headers={'content-type': "application/json"})
    #     self.assertEqual(response.status_code, 404)
    #     dataman = json.loads(response.get_data())
    #     self.assertEqual(dataman['message'], 'Email is required!')

    # #     #invalid email
    #     response = self.client.post('api/v1/auth/signup',
    #                              data=json.dumps(self.user_invalid_email),
    #                              headers={'content-type': "application/json"})
    #     self.assertEqual(response.status_code, 404)
    #     dataman = json.loads(response.get_data())
    #     self.assertEqual(dataman['message'], 'Email is invalid')
    # #     #no password
    #     response = self.client.post('api/v1/auth/signup',
    #                              data=json.dumps(self.user_no_password),
    #                              headers={'content-type': "application/json"})
    #     self.assertEqual(response.status_code, 404)
    #     dataman = json.loads(response.get_data())
    #     self.assertEqual(dataman['message'], 'Passord is required!')
     
    # #     #existing user
    #     response = self.client.post('api/v1/auth/signup',
    #                              data=json.dumps(self.user_existing),
    #                              headers={'content-type': "application/json"})
    #     self.assertEqual(response.status_code, 404)
    #     dataman = json.loads(response.get_data())
    #     self.assertEqual(dataman['message'], 'User already exists!')


    # #     #nopassword
    #     response = self.client.post('api/v1/auth/login',
    #                              data=json.dumps(self.no_password),
    #                              headers={'content-type': "application/json"})
    #     self.assertEqual(response.status_code, 404)
    #     dataman = json.loads(response.get_data())
    #     self.assertEqual(dataman['message'], 'Password is required')

    # #     #no username
    #     response = self.client.post('api/v1/auth/login',
    #                              data=json.dumps(self.no_username),
    #                              headers={'content-type': "application/json"})
    #     self.assertEqual(response.status_code, 404)
    #     dataman = json.loads(response.get_data())
    #     self.assertEqual(dataman['message'], 'Username is required')

    # #     #incorrect
    #     response = self.client.post('api/v1/auth/login',
    #                              data=json.dumps(self.wrong_login),
    #                              headers={'content-type': "application/json"})
    #     self.assertEqual(response.status_code, 401)
    #     dataman = json.loads(response.get_data())
    #     self.assertEqual(dataman['message'], 'Wrong password!')

    # #     #empty
    #     response = self.client.post('api/v1/auth/login',
    #                              data=json.dumps(self.correct_login),
    #                              headers={'content-type': "application/json"})
    #     self.assertEqual(response.status_code, 201)
    #     dataman = json.loads(response.get_data())
    #     self.assertEqual(dataman['message'], 'User logged in')

if __name__ == "__main__":
    unittest.main()     