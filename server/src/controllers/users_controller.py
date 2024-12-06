from flask import Blueprint, request
from src import db

users = Blueprint("users", __name__)


@users.route('/', methods=['GET'])
def main():
    return