from flask import Blueprint, request, render_template,redirect, flash
from src.services import members_services

members = Blueprint("members", __name__)


@members.route('/register', methods=['POST'])
def register():
    try:
        name = request.form.get('name', None)
        email = request.form.get('email', None)
        transportation_type = request.form.get('transportation_type', None)
        result = members_services.register(name=name, email=email, transportation_type=transportation_type)
        flash(result, 'success')
        return redirect('/members')
    except Exception as e:
        print("\nerror prompt:", e, "\n")
        flash(str(e), 'error')
        return redirect('/members/register')

        
@members.route('/', methods=['GET'])
def main():
    members = members_services.get_all_members()
    
    return render_template('members/list_members.html', members=members, title="Member List")

@members.route('/register', methods=['GET'])
def registration():
    return render_template('members/registration.html', title="Member Registration")