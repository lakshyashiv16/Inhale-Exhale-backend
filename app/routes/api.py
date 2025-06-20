from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User
from app import db

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/status', methods=['GET'])
def status():
    return {"status": "API is healthy"}

@api_blueprint.route('/signup', methods=['POST', 'OPTIONS'])
def signup():
    if request.method == 'OPTIONS':
        return '', 204
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    date_of_birth = data.get('date_of_birth')
    password = data.get('password')

    if not all([username, email, date_of_birth, password]):
        return jsonify({'error': 'Missing required fields'}), 400

    if User.query.filter((User.username == username) | (User.email == email)).first():
        return jsonify({'error': 'Username or email already exists'}), 409

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, email=email, date_of_birth=date_of_birth, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@api_blueprint.route('/login', methods=['POST', 'OPTIONS'])
def login():
    if request.method == 'OPTIONS':
        return '', 204
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not all([username, password]):
        return jsonify({'error': 'Missing username or password'}), 400

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        return jsonify({'message': 'Login successful', 'user': {'username': user.username, 'email': user.email, 'date_of_birth': user.date_of_birth}}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401
