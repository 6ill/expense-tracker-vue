from flask import Blueprint, request, session, jsonify
from src import db
from src.models.transaction import Transaction

transactions = Blueprint("transactions", __name__)


@transactions.route('/category/<category_name>')
def getByCategory(category_name):
    try:
        user = session.get('user')
        if not user: 
            return jsonify({"message": "You have not logged in!", "status": "failed"}), 401    
        
        transactions = Transaction.query.filter_by(user_id=user.get('id', -1), category=category_name).all()
        return jsonify({"transactions": transactions, "status": "success"}), 200
    
    except Exception as e:
        return jsonify({"message": "Failed to fetch transactions", "status": "failed", "error": str(e)}), 500

@transactions.route('/', methods=['POST'])
def create():
    try:
        data = request.json
        category = data.get('category')
        amount = data.get('amount')
        date = data.get('date')

        user = session.get('user')
        if not user: 
            return jsonify({"message": "You have not logged in!", "status": "failed"}), 401
        
        new_transaction = Transaction(user_id=user.get('id'), date=date, category=category, amount=amount)
        
        db.session.add(new_transaction)
        db.session.commit()

        return jsonify({"message": "New transaction has added successfully", "status": "success"}), 200
    except Exception as e:
        return jsonify({"message": "Failed to add new transaction. Please try again.", "status": "failed", "error": str(e)}), 500

