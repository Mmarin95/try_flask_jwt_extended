import json
import pytest

from app import app


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


def test_register(client):
    # Define test data
    data = {'username': 'testuser', 'password': 'testpass'}
    expected_message = {'message': 'User successfully registered!'}

    # Make POST request to /register endpoint
    response = client.post('/register', data=json.dumps(data),
                           content_type='application/json')

    # Check response status code and message
    assert response.status_code == 200
    assert json.loads(response.data) == expected_message


def test_login(client):
    # Define test data
    data = {'username': 'testuser', 'password': 'testpass'}

    # Make POST request to /login endpoint
    response = client.post('/login', data=json.dumps(data),
                           content_type='application/json')

    # Check response status code and access token format
    assert response.status_code == 200
    assert 'access_token' in json.loads(response.data)


def test_protected(client):
    # Define test data
    data = {'username': 'testuser', 'password': 'testpass'}

    # Make POST request to /login endpoint to get access token
    login_response = client.post(
        '/login', data=json.dumps(data), content_type='application/json')
    access_token = json.loads(login_response.data)['access_token']

    # Make GET request to /protected endpoint with access token
    response = client.get(
        '/protected', headers={'Authorization': f'Bearer {access_token}'})

    # Check response status code and message
    assert response.status_code == 200
    assert 'Hello, testuser!' in json.loads(response.data)['message']
