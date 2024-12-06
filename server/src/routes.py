from flask import Blueprint, redirect
from src.controllers.members_controller import members
from src.controllers.attendance_controller import attendance
from src.controllers.fees_controller import fees


# main blueprint to be registered with application
api = Blueprint('website', __name__)

@api.route('/', methods=['GET'])
def main():
    return redirect('/members')

# register user with api blueprint
api.register_blueprint(members, url_prefix="/members")
api.register_blueprint(attendance, url_prefix="/attendance")
api.register_blueprint(fees, url_prefix="/fees")

