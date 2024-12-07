from flask import Blueprint, request, session, jsonify
from src import db
from src.models.transaction import Transaction
from datetime import datetime

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

@transactions.route('/<int:transaction_id>', methods=['PUT'])
def update(transaction_id):
    try:
        data = request.json
        amount = data.get('amount')
        category = data.get('category')
        date = data.get('date')

        user = session.get('user')
        if not user :
            return jsonify({"message" : "You are not logged in", "status" : "failed"}), 401
        
        transaction = Transaction.query.filter_by(id=transaction_id)
        if not transaction :
            return jsonify({"message" : "Transaction not found", "status" : "failed"}), 404
        
        transaction.amount = amount
        transaction.category = category
        transaction.date = datetime.strptime(date, "%d-%m-%Y").date()

        db.session.commit()
        return jsonify({"message": "Transaction updated successfully", "status" : "success"}), 200
    
    except Exception as e:
        return jsonify({"message": "Update failed. Please try again.", "status": "failed", "error": str(e)}), 500