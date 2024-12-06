from flask import Blueprint, request
from src import db

transactions = Blueprint("transactions", __name__)


@transactions.route('/', methods=['GET'])
def main():
    return