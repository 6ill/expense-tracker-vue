from flask import Blueprint, request, render_template,redirect, flash
from src.services import fees_services

fees = Blueprint("fees", __name__)


        
@fees.route('/', methods=['GET'])
def main():
    fees = fees_services.get_all_fees()
    return render_template('fees/list_fees.html', fees = fees, title="Fee Payments")