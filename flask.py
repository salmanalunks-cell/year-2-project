
from flask import Flask, render_template, request, redirect, url_for

import json

attendance_app = Flask(__name__)

JSON_FILE = "attendance.json"
attendance = []





# Homepage
@attendance_app.route("/")
def home_page():

    return render_template("home.html")

@attendance_app.route("/attendance")
def activity_page():
    return render_template("activity.html")

# Main attendance dashboard
@attendance_app.route("/attendance")
def attendance_page():
    with open(JSON_FILE, "r") as doc:
            data = json.load(doc)
    

    student_attendance = data["student_attendance"]
    lecturer_attendance = data["lecturer_attendance"]

    context = {
        "student_count": len(student_attendance),
        "lecturer_count": len(lecturer_attendance),
        "total_count": len(student_attendance) + len(lecturer_attendance),
        "student_list": student_attendance,
        "lecturer_list": lecturer_attendance
    }

    return render_template("attendance.html", context=context)


# Student and lecturer attendance registration
@attendance_app.route("/add_attendance", methods=["GET", "POST"])
def add_attendance():
    if request.method == "POST":
        id = request.form.get("id")
        fname= request.form.get("first_name")
        lname = request.form.get("last_name")
        faculty= request.form.get("faculty")
        gender= request.form.get("gender")
        contact = request.form.get("contact")
        email = request.form.get("email")
        reg_no = request.form.get("reg_no")
        course = request.form.get("course")
        department = request.form.get("department")

        student_attendance = student_attendance(id, fname, lname, faculty,gender,contact,email,reg_no,course)
        lecturer_attendance = lecturer_attendance(id, fname, lname, faculty,gender,contact,email,department)

        attendance.append(student_attendance)
        attendance.append(lecturer_attendance)

        return redirect(url_for("tasks_page"))
    
    with open(attendance.json, "w") as doc:
          json.dump(attendance, doc, indent=4)
        

    return render_template("attendance.html")

# Run Flask application
if __name__ == "__main__":

    attendance_app.run(debug=True, port=7000)


