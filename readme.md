# Flask JWT Extended Example App

This is a simple Flask app that demonstrates how to use Flask JWT Extended to secure a RESTful API. The app provides three endpoints:

- `/register`: Allows users to register by creating a new account with a username and password.
- `/login`: Allows users to log in by providing their username and password, and returns a JWT access token if the login is successful.
- `/protected`: A protected endpoint that requires a valid JWT access token to access.

## Installation

1. Clone the repository:

```
git clone https://github.com/example/flask-jwt-extended-example.git
```

2. Install the required Python packages:

```
pip install -r requirements.txt
```

3. Start the Flask app:

```
export FLASK_APP=app.py
flask run
```

The app should now be running at [http://localhost:5000](http://localhost:5000).

## Usage

To use the app, you can send HTTP requests to the endpoints using a tool like `curl` or `httpie`. Here are some example requests:

### Register

```
http POST http://localhost:5000/register username=testuser password=testpass
```

### Login

```
http POST http://localhost:5000/login username=testuser password=testpass
```

The response should include a JSON object with an `access_token` field:

```
{
    "access_token": "<JWT access token>"
}
```

### Protected

To access the protected endpoint, you need to include the JWT access token in the `Authorization` header of the request:

```
http GET http://localhost:5000/protected "Authorization: Bearer <JWT access token>"
```

The response should include a JSON object with a `message` field that greets the authenticated user:

```
{
    "message": "Hello, testuser!"
}
```

## Tests

You can run the tests using the following command:

```
pytest test_app_pytest.py
```