from flask import Blueprint, request, render_template, flash, redirect
from src.services import attendance_services

attendance = Blueprint("attendance", __name__)


@attendance.route('/add-attendance', methods=['POST'])
def add_attendance():
    try:
        email = request.form.get('email', None)
        result = attendance_services.add_attendance(email)
        flash(result, 'success')
    except Exception as e:
        print("\nerror prompt:", e, "\n")
        flash(str(e), 'error')
    return redirect('/attendance')

@attendance.route('/', methods=['GET'])
def main():
    attendances = attendance_services.get_all_attendances()

    return render_template('attendances/attendence.html', attendances=attendances, title="Attendance List")
        
