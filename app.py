
from flask import Flask, render_template, request, redirect, url_for
import json

attendance_app = Flask(__name__)

JSON_FILE = "attendance.json"



@attendance_app.route("/main")
def main_page():

    with open(JSON_FILE, "r") as doc:
        data = json.load(doc)

    student_attendance = data["student_attendance"]
    lecturer_attendance = data["lecturer_attendance"]

    student_count = len(student_attendance)
    lecturer_count = len(lecturer_attendance)
    total_count = student_count + lecturer_count

    return render_template(
        "main.html",
        student_count=student_count,
        lecturer_count=lecturer_count,
        total_count=total_count,
        student_list=student_attendance,
        lecturer_list=lecturer_attendance
    )
# Registration page
@attendance_app.route("/")
def home_page():
    return render_template("index.html")


# Attendance dashboard
@attendance_app.route("/attendance")
def attendance_page():

    with open(JSON_FILE, "r") as doc:
        data = json.load(doc)

    student_attendance = data["student_attendance"]
    lecturer_attendance = data["lecturer_attendance"]

    print("STUDENTS:", student_attendance)
    print("LECTURERS:", lecturer_attendance)

    student_count = len(student_attendance)
    lecturer_count = len(lecturer_attendance)
    total_count = student_count + lecturer_count
    
    return render_template(
       "project.html",
        student_count=student_count,
        lecturer_count=lecturer_count,
        total_count=total_count,
        student_list=student_attendance,
        lecturer_list=lecturer_attendance
    )
    

# Add student and lecturer
@attendance_app.route("/add_attendance", methods=["POST"])
def add_attendance():

    firstname = request.form.get("first_name")
    lastname = request.form.get("last_name")
    reg_no = request.form.get("reg_no")
    course = request.form.get("course")
    category = request.form.get("category")
    date = request.form.get("date")
    status = request.form.get("status")

    with open(JSON_FILE, "r") as doc:
        data = json.load(doc)

    record = {
        "id":len(data["student_attendance"]) + len(data["lecturer_attendance"]) + 1,
        "first_name": firstname,
        "last_name": lastname,
        "registration": reg_no,
        "course": course,
        "category": category,
        "date": date,
        "status": status,
    }

    if category == "student":
        
        data["student_attendance"].append(record)

    elif category == "lecturer":
        data["lecturer_attendance"].append(record)

    else:
        return "Please select Student or Lecturer."

    with open(JSON_FILE, "w") as doc:
        json.dump(data, doc, indent=4)

    return redirect(url_for("main_page"))



if __name__ == "__main__":
    attendance_app.run(debug=True, port=7000)

