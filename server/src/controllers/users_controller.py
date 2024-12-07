from flask import Blueprint, request, session, jsonify
from src import db
from src.models.user import User
from src.models.limit import Limit
from werkzeug.security import generate_password_hash, check_password_hash

users = Blueprint("users", __name__)


@users.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        # Validate input
        if not username or not password:
            return jsonify({"message": "Username and password are required", "status": "failed"}), 400

        # Check if user already exists
        user = User.query.filter_by(username=username).first()
        if user:
            return jsonify({"message": "User with this username already exists!", "status": "failed"}), 400

        # Create a new user
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)

        # Create new limit
        new_limit = Limit(user_id=new_user.id, food=0, lifestyle=0, travel=0, entertainment=0, other=0)
        db.session.add(new_limit)
        db.session.commit()

        return jsonify({"message": "You have been registered successfully!", "status": "success"}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Registration failed. Please try again.", "status": "failed", "error": str(e)}), 500


@users.route('/login', methods=['POST'])
def login():
    try:
        # Get data from JSON payload
        data = request.json
        username = data.get('username')
        password = data.get('password')

        # Check if user exists
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return jsonify({"message": "Invalid username or password", "status": "failed"}), 401

        # Set session
        session['user'] = {'id': user.id, 'username': user.username}
        session['is_authenticated'] = True

        return jsonify({"message": "Login successfully", "status": "success"}), 200

    except Exception as e:
        return jsonify({"message": "Login failed. Please try again.", "status": "failed", "error": str(e)}), 500

@users.route('/logout', methods=['POST'])
def logout():
    try:
        session.pop('user', None)
        session.pop('is_authenticated', None)
        return jsonify({"message": "Logout successfully", "status": "success"}), 200
    except Exception as e:
        return jsonify({"message": "Logout failed. Please try again.", "status": "failed", "error": str(e)}), 500
    