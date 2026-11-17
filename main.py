
import json
from project import *

while True:
    print("\n1. Course registration\n2. Add course units\n3. Student Registration\n4. Lecturer Registration\n5. Timetable\n6. Study Session\n7. Student Attendance\n8. Lecturer Attendance\n9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        while True:
            course_id = Course.generate_id()
            course_name = input("Enter course name: ")
            course_code = input("Enter course code: ")
            faculty = input("Enter faculty: ")

            course = Course(course_id, course_name, course_code, faculty)

            new_course = {
                "course_id": course.course_id,
                "course_name": course.course_name,
                "course_code": course.course_code,
                "faculty": course.faculty
            }

            with open("course.json", "r") as doc:
                Course_list = json.load(doc)

            with open("course.json", "w") as doc:
                Course_list.append(new_course)
                json.dump(Course_list, doc, indent=4)

            print(course)

            add_course = input("Do you want to add another course(Y/N): ")
            if add_course == "Y":
                continue
            else:
                break

    elif choice == "2":
        while True:
            courseunit_id = CourseUnit.generate_id()
            courseunit_name = input("Enter course unit name: ")
            courseunit_code = input("Enter course unit code: ")
            course = input("Enter course: ")
            credit_units = input("Enter credit units: ")

            courseunit = CourseUnit(courseunit_id, courseunit_name, courseunit_code, course, credit_units)

            new_courseunit = {
                "courseunit_id": courseunit.courseunit_id,
                "courseunit_name": courseunit.courseunit_name,
                "courseunit_code": courseunit.courseunit_code,
                "course": courseunit.course,
                "credit_units": courseunit.credit_units
            }

            with open("courseunit.json", "r") as doc:
                CourseUnit_list = json.load(doc)

            with open("courseunit.json", "w") as doc:
                CourseUnit_list.append(new_courseunit)
                json.dump(CourseUnit_list, doc, indent=4)

            print(courseunit)

            add_courseunit = input("Do you want to add another course unit(Y/N): ")
            if add_courseunit == "Y":
                continue
            else:
                break

    elif choice == "3":
        while True:
            student_id = Student.generate_id()
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            contact = input("Enter contact: ")
            reg_no = input("Enter registration number: ")
            year_of_study = input("Enter year of study: ")
            gender = input("Enter gender: ")
            course = input("Enter course: ")

            student = Student(student_id, first_name, last_name, contact, reg_no, year_of_study, gender, course)

            new_student = {
                "student_id": student.student_id,
                "first_name": student.first_name,
                "last_name": student.last_name,
                "contact": student.contact,
                "reg_no": student.reg_no,
                "year_of_study": student.year_of_study,
                "gender": student.gender,
                "course": student.course,
                "email": student.get_email()
            }

            with open("student.json", "r") as doc:
                Student_list = json.load(doc)

            with open("student.json", "w") as doc:
                Student_list.append(new_student)
                json.dump(Student_list, doc, indent=4)

            print(student)

            add_student = input("Do you want to add another student(Y/N): ")
            if add_student == "Y":
                continue
            else:
                break

    elif choice == "4":
        while True:
            lecturer_id = Lecturer.generate_id()
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            faculty = input("Enter faculty: ")
            gender = input("Enter gender: ")
            contact = input("Enter contact: ")
            department = input("Enter department: ")

            lecturer = Lecturer(lecturer_id, first_name, last_name, faculty, gender, contact, department)

            new_lecturer = {
                "lecturer_id": lecturer.lecturer_id,
                "first_name": lecturer.first_name,
                "last_name": lecturer.last_name,
                "faculty": lecturer.faculty,
                "gender": lecturer.gender,
                "contact": lecturer.contact,
                "department": lecturer.department,
                "email": lecturer.get_email()
            }

            with open("lecturer.json", "r") as doc:
                Lecturer_list = json.load(doc)

            with open("lecturer.json", "w") as doc:
                Lecturer_list.append(new_lecturer)
                json.dump(Lecturer_list, doc, indent=4)

            print(lecturer)

            add_lecturer = input("Do you want to add another lecturer(Y/N): ")
            if add_lecturer == "Y":
                continue
            else:
                break

    elif choice == "5":
        while True:
            with open("studysession.json", "r") as doc:
                Studysession_list = json.load(doc)

            study_session_id = input("Enter study session ID: ")

            for session in Studysession_list:
                if session["study_session_id"] == study_session_id:
                    studysession = Studysession(
                        session["study_session_id"],
                        session["academic_year"],
                        session["semester"]
                    )

                    studysession.load_timetables(session["timetables"])

                    timetable_id = Timetable.generate_id()
                    day = input("Enter day: ")
                    course_unit = input("Enter course unit: ")
                    lecturer = input("Enter lecturer: ")
                    start_time = input("Enter start time: ")
                    end_time = input("Enter end time: ")

                    timetable = Timetable(timetable_id, day, course_unit, lecturer, start_time, end_time)

                    studysession.add_timetable(timetable)
                    studysession.save_timetables()

                    new_timetable = {
                        "session": timetable.session,
                        "day": timetable.day,
                        "course_unit": timetable.course_unit,
                        "lecturer": timetable.lecturer,
                        "start_time": timetable.start_time,
                        "end_time": timetable.end_time
                    }

                    with open("timetable.json", "r") as doc:
                        Timetable_list = json.load(doc)

                    with open("timetable.json", "w") as doc:
                        Timetable_list.append(new_timetable)
                        json.dump(Timetable_list, doc, indent=4)

                    break
            else:
                print("Study session not found")

            add_timetable = input("Do you want to add more timetable(Y/N): ")
            if add_timetable == "Y":
                continue
            else:
                break

    elif choice == "6":
        while True:
            study_session_id = Studysession.generate_id()
            academic_year = input("Enter academic year: ")
            semester = input("Enter semester: ")

            studysession = Studysession(study_session_id, academic_year, semester)

            new_studysession = {
                "study_session_id": studysession.study_session_id,
                "academic_year": studysession.academic_year,
                "semester": studysession.semester,
                "timetables": []
            }

            with open("studysession.json", "r") as doc:
                Studysession_list = json.load(doc)

            with open("studysession.json", "w") as doc:
                Studysession_list.append(new_studysession)
                json.dump(Studysession_list, doc, indent=4)

            print(studysession)

            add_studysession = input("Do you want to add another study session(Y/N): ")
            if add_studysession == "Y":
                continue
            else:
                break

    elif choice == "7":
        while True:
            attendance_id = StudentAttendance.generate_id()
            date = input("Enter date: ")
            student = input("Enter student ID: ")

            attendance = StudentAttendance(attendance_id, date, student)

            new_attendance = {
                "id": attendance.id,
                "date": attendance.date,
                "student": attendance.student,
                "status": attendance.get_status()
            }

            with open("studentattendance.json", "r") as doc:
                StudentAttendance_list = json.load(doc)

            with open("studentattendance.json", "w") as doc:
                StudentAttendance_list.append(new_attendance)
                json.dump(StudentAttendance_list, doc, indent=4)

            print(attendance)

            add_attendance = input("Do you want to add another student attendance(Y/N): ")
            if add_attendance == "Y":
                continue
            else:
                break

    elif choice == "8":
        while True:
            attendance_id = LecturerAttendance.generate_id()
            date = input("Enter date: ")
            lecturer = input("Enter lecturer ID: ")

            attendance = LecturerAttendance(attendance_id, date, lecturer)

            new_attendance = {
                "id": attendance.id,
                "date": attendance.date,
                "lecturer": attendance.lecturer,
                "status": attendance.get_status()
            }

            with open("lecturerattendance.json", "r") as doc:
                LecturerAttendance_list = json.load(doc)

            with open("lecturerattendance.json", "w") as doc:
                LecturerAttendance_list.append(new_attendance)
                json.dump(LecturerAttendance_list, doc, indent=4)

            print(attendance)

            add_attendance = input("Do you want to add another lecturer attendance(Y/N): ")
            if add_attendance == "Y":
                continue
            else:
                break

    elif choice == "9":
        break

    else:
        print("Invalid choice")

