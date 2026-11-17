import json
from project import (
    CourseUnit, Student, Lecturer, Course, 
    Studysession, Timetable, StudentAttendance, LecturerAttendance
)


def load_json_file(filename):
    try:
        with open(filename, "r") as doc:
            return json.load(doc)
    except FileNotFoundError:
        return []


while True:
    print("\n1. Course registration\n2. Add course units\n3. Student Registration\n4. Lecturer Registration\n5. Timetable\n6. Study Session\n7. Student Attendance\n8. Lecturer Attendance\n9. Exit\n")
    choice = input("Enter your choice (1-9): ")

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

            course_list = load_json_file("course.json")
            course_list.append(new_course)

            with open("course.json", "w") as doc:
                json.dump(course_list, doc, indent=4)

            print("Course registered successfully!")
            if input("Do you have more courses to add (Y/N): ").strip().upper() != "Y":
                break

    elif choice == "2":
        while True:
            courseunit_list = load_json_file("courseunit.json")

            courseunit_id = "CU-" + str(len(courseunit_list) + 1)
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

            courseunit_list.append(new_courseunit)
            with open("courseunit.json", "w") as doc:
                json.dump(courseunit_list, doc, indent=4)

            print("Course unit added successfully!")
            if input("Do you have more course units to add (Y/N): ").strip().upper() != "Y":
                break

    elif choice == "3":
        while True:
            print("--- Enter Student Course Details ---")
            c_id = Course.generate_id()
            c_name = input("Enter course name: ")
            c_code = input("Enter course code: ")
            c_fac = input("Enter faculty: ")
            my_course = Course(c_id, c_name, c_code, c_fac)

            student_list = load_json_file("student.json")

            student_id = "S-" + str(len(student_list) + 1)
            student_first_name = input("Enter student's first name: ")
            student_last_name = input("Enter student's last name: ")
            contact = input("Enter student contact number: ")
            registration_number = input("Enter student registration number: ")
            year_of_study = input("Enter year of study: ")
            gender = input("Enter student gender: ")

            student = Student(student_id, student_first_name, student_last_name, contact, registration_number, year_of_study, gender, my_course)

            new_student = {
                "student_id": student.student_id,
                "student_first_name": student.first_name,
                "student_last_name": student.last_name,
                "contact": student.contact,
                "registration_number": student.reg_no,
                "year_of_study": student.year_of_study,
                "gender": student.gender,
                "email": student.get_email(),
                "course": {
                    "course_id": student.course.course_id,
                    "course_name": student.course.course_name,
                    "course_code": student.course.course_code,
                    "faculty": student.course.faculty
                }
            }

            student_list.append(new_student)
            with open("student.json", "w") as doc:
                json.dump(student_list, doc, indent=4)

            print("Student registered successfully!")
            if input("Do you have more students to add (Y/N): ").strip().upper() != "Y":
                break

    elif choice == "4":
        while True:
            lecturer_list = load_json_file("lecturer.json")

            lecturer_id = "L-" + str(len(lecturer_list) + 1)
            lecturer_first_name = input("Enter Lecturer's first name: ")
            lecturer_last_name = input("Enter lecturer's last name: ")
            faculty = input("Enter the faculty: ")
            gender = input("Enter the gender: ")
            contact = input("Enter Lecturer's contact: ")
            department = input("Enter the department: ")

            lecturer = Lecturer(lecturer_id, lecturer_first_name, lecturer_last_name, faculty, gender, contact, department)

            new_lecturer = {
                "lecturer_id": lecturer.lecturer_id,
                "lecturer_first_name": lecturer.first_name,
                "lecturer_last_name": lecturer.last_name,
                "faculty": lecturer.faculty,
                "gender": lecturer.gender,
                "contact": lecturer.contact,
                "department": lecturer.department,
                "email": lecturer.get_email()
            }

            lecturer_list.append(new_lecturer)
            with open("lecturer.json", "w") as doc:
                json.dump(lecturer_list, doc, indent=4)

            print("Lecturer registered successfully!")
            if input("Do you have more lecturers to add (Y/N): ").strip().upper() != "Y":
                break

    elif choice == "5":
        while True:
            studysession_list = load_json_file("studysession.json")
            study_session_id = input("Enter study session ID (e.g., SS-1): ")

            session_found = False
            for session_data in studysession_list:
                if session_data["study_session_id"] == study_session_id:
                    session_found = True
                    studysession = Studysession(
                        session_data["study_session_id"],
                        session_data["academic_year"],
                        session_data["semester"]
                    )
                    studysession.load_timetables(session_data.get("timetables", []))

                    session_name = input("Enter session name/type (e.g., Morning/Evening): ")
                    day = input("Enter day: ")
                    course_unit = input("Enter course unit: ")
                    lecturer = input("Enter lecturer: ")
                    start_time = input("Enter start time: ")
                    end_time = input("Enter end time: ")

                    timetable = Timetable(
                        session_name, day, course_unit,
                        lecturer, start_time, end_time
                    )

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

                    timetable_list = load_json_file("timetable.json")
                    timetable_list.append(new_timetable)

                    with open("timetable.json", "w") as doc:
                        json.dump(timetable_list, doc, indent=4)

                    print("Timetable added successfully!")
                    break

            if not session_found:
                print("Study session not found.")

            if input("Do you want to add more timetables (Y/N): ").strip().upper() != "Y":
                break

    elif choice == "6":
        while True:
            studysession_list = load_json_file("studysession.json")

            study_session_id = Studysession.generate_id()
            academic_year = input("Enter the academic year: ")
            semester = input("Enter the semester: ")

            studysession = Studysession(study_session_id, academic_year, semester)

            timetables_for_session = []
            while True:
                add_now = input("Do you want to add a timetable to this study session now? (Y/N): ").strip().upper()
                if add_now == "Y":
                    session_name = input("Enter session name/type (e.g., Morning/Evening): ")
                    day = input("Enter day: ")
                    course_unit = input("Enter course unit: ")
                    lecturer = input("Enter lecturer: ")
                    start_time = input("Enter start time: ")
                    end_time = input("Enter end time: ")

                    timetable_data = {
                        "session": session_name,
                        "day": day,
                        "course_unit": course_unit,
                        "lecturer": lecturer,
                        "start_time": start_time,
                        "end_time": end_time
                    }
                    timetables_for_session.append(timetable_data)
                    print("Timetable added to this session!")
                else:
                    break

            new_studysession = {
                "study_session_id": studysession.study_session_id,
                "academic_year": studysession.academic_year,
                "semester": studysession.semester,
                "timetables": timetables_for_session
            }

            studysession_list.append(new_studysession)
            with open("studysession.json", "w") as doc:
                json.dump(studysession_list, doc, indent=4)

            print(f"Study session '{study_session_id}' created successfully with {len(timetables_for_session)} timetable(s)!")
            if input("Do you want to add more study sessions (Y/N): ").strip().upper() != "Y":
                break

    elif choice == "7":
        while True:
            studentattendance_list = load_json_file("studentattend.json")

            attendance_id = "SA-" + str(len(studentattendance_list) + 1)
            date = input("Enter the date (dd/mm/yyyy): ")
            student_id = input("Enter student id (S-1): ")

            studentattendance = StudentAttendance(attendance_id, date, student_id)

            new_studentattendance = {
                "studentattendance_id": studentattendance.id,
                "date": studentattendance.date,
                "student": studentattendance.student,
                "status": studentattendance.get_status
            }

            studentattendance_list.append(new_studentattendance)
            with open("studentattend.json", "w") as doc:
                json.dump(studentattendance_list, doc, indent=4)

            print("Student attendance recorded successfully!")
            if input("Do you want to add more student attendance records (Y/N): ").strip().upper() != "Y":
                break

    elif choice == "8":
        while True:
            lecturerattendance_list = load_json_file("lecturerattend.json")

            lecturerattendance_id = "LA-" + str(len(lecturerattendance_list) + 1)
            date = input("Enter the date (dd/mm/yyyy): ")
            lecturer_id = input("Enter the lecturer id (L-1): ")

            lecturerattendance = LecturerAttendance(lecturerattendance_id, date, lecturer_id)

            new_lecturerattendance = {
                "lecturerattendance_id": lecturerattendance.id,
                "date": lecturerattendance.date,
                "lecturer": lecturerattendance.lecturer,
                "status": lecturerattendance.get_status
            }

            lecturerattendance_list.append(new_lecturerattendance)
            with open("lecturerattend.json", "w") as doc:
                json.dump(lecturerattendance_list, doc, indent=4)

            print("Lecturer attendance recorded successfully!")
            if input("Do you want to add more lecturer attendance records (Y/N): ").strip().upper() != "Y":
                break

    elif choice == "9":
        print("You have exited the program")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 9.")
