import unittest
import json

from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_register(self):
        # Define test data
        data = {'username': 'testuser', 'password': 'testpass'}
        expected_message = {'message': 'User successfully registered!'}

        # Make POST request to /register endpoint
        response = self.app.post(
            '/register', data=json.dumps(data), content_type='application/json')

        # Check response status code and message
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), expected_message)

    def test_login(self):
        # Define test data
        data = {'username': 'testuser', 'password': 'testpass'}

        # Make POST request to /login endpoint
        response = self.app.post(
            '/login', data=json.dumps(data), content_type='application/json')

        # Check response status code and access token format
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', json.loads(response.data))

    def test_protected(self):
        # Define test data
        data = {'username': 'testuser', 'password': 'testpass'}

        # Make POST request to /login endpoint to get access token
        login_response = self.app.post(
            '/login', data=json.dumps(data), content_type='application/json')
        access_token = json.loads(login_response.data)['access_token']

        # Make GET request to /protected endpoint with access token
        response = self.app.get(
            '/protected', headers={'Authorization': f'Bearer {access_token}'})

        # Check response status code and message
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello, testuser!', json.loads(response.data)['message'])
