"""
This module handles API routes.
"""
from flask import Blueprint, request, jsonify
from api.models import db, User
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token, jwt_required

api = Blueprint('api', __name__)
bcrypt = Bcrypt()

# Allow CORS
CORS(api)

@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():
    """Simple hello endpoint to check connectivity."""
    response_body = {
        "message": "Hello! I'm a message that came from the backend."
    }
    return jsonify(response_body), 200

@api.route('/signup', methods=['POST'])
def signup():
    """Register a new user."""
    email = request.json.get('email')
    password = request.json.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "User already exists"}), 400

    new_user = User(email=email)
    new_user.set_password(password)

    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "User created successfully"}), 201


@api.route('/login', methods=['POST'])
def login():
    """Authenticate user and return a JWT token."""
    email = request.json.get('email')
    password = request.json.get('password')

    user = User.query.filter_by(email=email).first()

    if user and bcrypt.check_password_hash(user.password, password):
        token = create_access_token(identity={'email': user.email})
        return jsonify(access_token=token), 200

    return jsonify({"error": "Invalid credentials"}), 401

@api.route('/private', methods=['GET'])
@jwt_required()
def private():
    """Access protected route for authenticated users."""
    return jsonify(message="Welcome to the private area!"), 200
