from flask import Blueprint, request
from src import db

limits = Blueprint("limits", __name__)


@limits.route('/', methods=['GET'])
def main():
    return