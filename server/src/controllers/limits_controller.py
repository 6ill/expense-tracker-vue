from flask import Blueprint, request, session, jsonify
from src.models.limit import Limit
from src import db

limits = Blueprint("limits", __name__)


@limits.route('/', methods=['PUT'])
def update(user_id):
    try:
        data = request.json
        type = data.get('type')
        budget = data.get('budget')

        user = session.get('user')
        if not user: 
            return jsonify({"message": "You have not logged in", "status": "failed"}), 401
        
        limit_data = Limit.query.filter_by(user_id=session['user']['id']).first()
        if not limit_data:
            return jsonify({"message": "Data not found", "status": "failed"}), 401
        
        # Update limit_data
        setattr(limit_data, type, budget)
        db.session.commit()
        return jsonify({"message": "Update successfully", "status": "success"}), 200
    
    except Exception as e:
        return jsonify({"message": "Update budget failed. Please try again.", "status": "failed", "error": str(e)}), 500
    
@limits.route('/', methods=['GET'])
def getBudgetLimit():
    try:
        user = session.get('user')
        if not user: 
            return jsonify({"message": "You have not logged in", "status": "failed"}), 401
        
        limit_data = Limit.query.filter_by(user_id=user.get('id')).first()
        if not limit_data:
            return jsonify({"message": "Data not found", "status": "failed"}), 401
        
        
        return jsonify({"limits": limit_data, "status": "success"}), 200
    
    except Exception as e:
        return jsonify({"message": "Failed to fetch limit data.", "status": "failed", "error": str(e)}), 500
