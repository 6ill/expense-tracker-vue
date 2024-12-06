from flask import Blueprint, request, session, jsonify
from src import db
from src.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash

users = Blueprint("users", __name__)


@users.route('/register', methods=['POST'])
def register():
    try:
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        if user:
            raise Exception("User with this username has already registered!")
        
        if not user:
            raise Exception("No user")

        if not password:
            raise Exception("No password")
        
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "You have been register successfully!", "status": "success"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e), "status": "failed"})


@users.route('/login', methods=['POST'])    
def login():
    try:
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if not user or not check_password_hash(user.password, password):
            return {"message": "Please check your login details and try again.", "status": "failed"}
        
        session['user'] = {'id': user.id, 'username': user.username}
        session['is_authenticated'] = True

        return jsonify({"message": "Login successfully", "status": "success"})
    except Exception as e: 
        return jsonify({"message": str(e), "status": "failed"})
