from flask import Blueprint, request, session
from src import db
from src.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash

users = Blueprint("users", __name__)


@users.route('/register', methods=['POST'])
def register():
    try:
        username = request.form.get('username')
        name = request.form.get('name')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        if user:
            raise Exception("User with this username has already registered!")
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, name=name, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return {"message": "You have been register successfully!", "status": "success"}
    except Exception as e:
        db.session.rollback()
        return {"message": e, "status": "failed"}


@users.route('/login', methods=['POST'])    
def login():
    try:
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if not user or not check_password_hash(user.password, password):
            return {"message": "Please check your login details and try again.", "status": "failed"}
        
        session['user'] = {'id': user.id, 'username': user.username, 'name': user.name}
        session['is_authenticated'] = True

        return {"message": "Login successfully", "status": "success"}
    except Exception as e: 
        return {"message": e, "status": "failed"}
