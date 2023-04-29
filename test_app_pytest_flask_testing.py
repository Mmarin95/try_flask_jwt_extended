from app import app
from flask_testing import TestCase
import json


class TestApp(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['JWT_SECRET_KEY'] = 'test-secret'
        return app

    def test_register(self):
        # Define test data
        data = {'username': 'testuser', 'password': 'testpass'}
        expected_message = {'message': 'User successfully registered!'}

        # Make POST request to /register endpoint
        response = self.client.post(
            '/register', data=json.dumps(data), content_type='application/json')

        # Check response status code and message
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), expected_message)

    def test_login(self):
        # Define test data
        data = {'username': 'testuser', 'password': 'testpass'}

        # Make POST request to /login endpoint
        response = self.client.post(
            '/login', data=json.dumps(data), content_type='application/json')

        # Check response status code and access token format
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', json.loads(response.data))

    def test_protected(self):
        # Define test data
        data = {'username': 'testuser', 'password': 'testpass'}

        # Make POST request to /login endpoint to get access token
        login_response = self.client.post(
            '/login', data=json.dumps(data), content_type='application/json')
        access_token = json.loads(login_response.data)['access_token']

        # Make GET request to /protected endpoint with access token
        response = self.client.get(
            '/protected', headers={'Authorization': f'Bearer {access_token}'})

        # Check response status code and message
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello, testuser!', json.loads(response.data)['message'])
