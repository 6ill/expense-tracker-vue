from flask import Blueprint, request, session, jsonify
from src import db
from src.models.transaction import Transaction
from datetime import datetime

transactions = Blueprint("transactions", __name__)


@transactions.route('/category/<category_name>')
def getByCategory(category_name, methods=['GET']):
    try:
        user = session.get('user')
        if not user: 
            return jsonify({"message": "You have not logged in!", "status": "failed"}), 401    
        
        transactions_data = Transaction.query.filter_by(user_id=user.get('id', -1), category=category_name).all()
        transactions = [transaction.to_dict() for transaction in transactions_data]
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
        desc = data.get('description')

        user = session.get('user')
        if not user: 
            return jsonify({"message": "You have not logged in!", "status": "failed"}), 401
        
        new_transaction = Transaction(user_id=user.get('id'), date=date, category=category, amount=amount, desc=desc)
        
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
        desc = data.get('description')

        user = session.get('user')
        if not user :
            return jsonify({"message" : "You are not logged in", "status" : "failed"}), 401
        
        transaction = Transaction.query.filter_by(id=transaction_id).first()
        if not transaction :
            return jsonify({"message" : "Transaction not found", "status" : "failed"}), 404
        
        transaction.amount = amount
        transaction.category = category
        transaction.date = date
        transaction.desc = desc

        db.session.commit()
        return jsonify({"message": "Transaction updated successfully", "status" : "success"}), 200
    
    except Exception as e:
        return jsonify({"message": "Update failed. Please try again.", "status": "failed", "error": str(e)}), 500
    

@transactions.route('/<int:transaction_id>', methods=['GET'])
def get_transaction_by_id(transaction_id):
    try:
       
        user = session.get('user')
        if not user :
            return jsonify({"message" : "You are not logged in", "status" : "failed"}), 401
        
        transaction = Transaction.query.filter_by(id=transaction_id).first()
        if not transaction :
            return jsonify({"message" : "Transaction not found", "status" : "failed"}), 404
        
        return jsonify({"transaction": transaction.to_dict(), "status" : "success"}), 200
    
    except Exception as e:
        return jsonify({"message": "Update failed. Please try again.", "status": "failed", "error": str(e)}), 500
    

@transactions.route('/<int:transaction_id>', methods=['DELETE'])
def delete_transaction_by_id(transaction_id):
    try:
        user = session.get('user')
        if not user :
            return jsonify({"message" : "You are not logged in", "status" : "failed"}), 401
        
        transaction = Transaction.query.filter_by(id=transaction_id).first()
        if not transaction :
            return jsonify({"message" : "Transaction not found", "status" : "failed"}), 404

        db.session.delete(transaction)
        db.session.commit()
        return jsonify({"message": "Transaction updated successfully", "status" : "success"}), 200
    
    except Exception as e:
        return jsonify({"message": "Update failed. Please try again.", "status": "failed", "error": str(e)}), 500