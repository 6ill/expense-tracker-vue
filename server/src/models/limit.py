from datetime import datetime
from src import db

class Limit(db.Model):
    __tablename__ = 'limit'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    food = db.Column(db.Float, nullable=False)
    lifestyle = db.Column(db.Float, nullable=False)
    travel = db.Column(db.Float, nullable=False)
    entertainment = db.Column(db.Float, nullable=False)
    other = db.Column(db.Float, nullable=False)

    
    


    