from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
# Replace with a strong secret key in production
app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)


@app.route('/register', methods=['POST'])
def register():
    # Get user data from request
    username = request.json.get('username')
    password = request.json.get('password')

    # Store user data in database (not shown)

    # Return success message
    return jsonify({'message': 'User successfully registered!'})


@app.route('/login', methods=['POST'])
def login():
    # Get user data from request
    username = request.json.get('username')
    password = request.json.get('password')

    # Check if user exists and password is correct (not shown)

    # Generate access token and return it
    access_token = create_access_token(identity=username)
    return jsonify({'access_token': access_token})


@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    # Get user identity from JWT
    current_user = get_jwt_identity()

    # Return success message
    return jsonify({'message': f'Hello, {current_user}!'})


if __name__ == '__main__':
    app.run(debug=True)
