from flask import Blueprint, redirect
from src.controllers.users_controller import users
from src.controllers.transactions_controller import transactions
from src.controllers.limits_controller import limits

# main blueprint to be registered with application
api = Blueprint('api', __name__)


# register user with api blueprint
api.register_blueprint(transactions, url_prefix="/transactions")
api.register_blueprint(limits, url_prefix="/limits")
api.register_blueprint(users, url_prefix="/users")

