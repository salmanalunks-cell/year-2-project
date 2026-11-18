
from project import CourseUnit, Student, Lecturer, Course, Studysession, Timetable, StudentAttendance, LecturerAttendance
import json


def load_records(filename):
    with open(filename, "r", encoding="utf-8") as doc:
        records = json.load(doc)
    return records


def save_records(filename, records):
    with open(filename, "w", encoding="utf-8") as doc:
        json.dump(records, doc, indent=4)


Course_list = []
Student_list = []
Lecturer_list = []
Courseunit_list = []
Timetable_list = []
Studysession_list = []
StudentAttendance_list = []
LecturerAttendance_list = []


while True:
    print("\n1.Course registration\n2.Add course units\n3.Student Registration\n4.Lecturer Registration\n5.Timetable\n6.Study Session\n7.Student Attendance\n8.Lecturer Attendance\n9.Exit\n")
    choice = input("Enter your choice(1-9): ")

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

            Course_list = load_records("course.json")
            Course_list.append(new_course)
            save_records("course.json", Course_list)

            add_course = input("Do you have more courses to add (Y/N): ")
            if add_course == "Y":
                continue
            else:
                break

    elif choice == "2":
        while True:
            courseunit_id = CourseUnit.generate_id()
            courseunit_name = input("Enter course unit name: ")
            courseunit_code = input("Enter course unit code: ")
            course = input("Enter course name or code: ")
            credit_units = input("Enter credit units: ")

            # CourseUnit requires five arguments, including the course.
            courseunit = CourseUnit(courseunit_id, courseunit_name, courseunit_code, course, credit_units)

            new_courseunit = {
                "courseunit_id": courseunit.courseunit_id,
                "courseunit_name": courseunit.courseunit_name,
                "courseunit_code": courseunit.courseunit_code,
                "course": courseunit.course,
                "credit_units": courseunit.credit_units
            }

            Courseunit_list = load_records("courseunit.json")
            Courseunit_list.append(new_courseunit)
            save_records("courseunit.json", Courseunit_list)

            add_courseunit = input("Do you have more coursunits to add(Y/N): ")
            if add_courseunit == "Y":
                continue
            else:
                break

    elif choice == "3":
        while True:
            my_course = Course("C1010", "computer science", "BSCS", "Faculty of Science")

            student_id = Student.generate_id()
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
                "course": student.course.__dict__
            }

            Student_list = load_records("student.json")
            Student_list.append(new_student)
            save_records("student.json", Student_list)

            add_student = input("Do you have more students to add (Y/N): ")
            if add_student == "Y":
                continue
            else:
                break

    elif choice == "4":
        while True:
            lecturer_id = Lecturer.generate_id()
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
                # Keep the key consistent with the student email field (no trailing space).
                "email": lecturer.get_email()
            }

            Lecturer_list = load_records("lecturer.json")
            Lecturer_list.append(new_lecturer)
            save_records("lecturer.json", Lecturer_list)

            add_lecturer = input("Do you have more lecturers to add (Y/N): ")
            if add_lecturer == "Y":
                continue
            else:
                break

    elif choice == "5":
        while True:
            session = Timetable.generate_id()
            day = input("Enter day: ")
            course_unit = input("Enter course unit: ")
            lecturer = input("Enter lecturer: ")
            start_time = input("Enter start time: ")
            end_time = input("Enter end time: ")

            timetable = Timetable(session, day, course_unit, lecturer, start_time, end_time)

            new_timetable = {
                "session": timetable.session,
                "day": timetable.day,
                "course_unit": timetable.course_unit,
                "lecturer": timetable.lecturer,
                "start_time": timetable.start_time,
                "end_time": timetable.end_time
            }

            Timetable_list = load_records("timetable.json")
            Timetable_list.append(new_timetable)
            save_records("timetable.json", Timetable_list)

            add_timetable = input("Do you want to add more timetable(Y/N): ")
            if add_timetable == "Y":
                continue
            else:
                break


    
    elif choice == "6":
        while True:
            study_session_id = Studysession.generate_id()
            academic_year = input("Enter the academic year: ")
            semester = input("Enter the semester: ")

            print("Available timetables:")
            available_timetables = load_records("timetable.json")

            number = 1

            for timetable_data in available_timetables:
                print(f"{number}. {timetable_data['session']} | {timetable_data['day']} | {timetable_data['course_unit']} | {timetable_data['lecturer']} | {timetable_data['start_time']} - {timetable_data['end_time']}")
                number += 1

            timetable_choice = int(input("Choose a timetable number: "))

            my_timetable = Timetable(**available_timetables[timetable_choice - 1])

            studysession = Studysession(study_session_id, academic_year, semester, my_timetable)

            new_studysession = {
                "study_session_id": studysession.study_session_id,
                "academic_year": studysession.academic_year,
                "semester": studysession.semester,
                "timetable": {
                    "session": my_timetable.session,
                    "day": my_timetable.day,
                    "course_unit": my_timetable.course_unit,
                    "lecturer": my_timetable.lecturer,
                    "start_time": my_timetable.start_time,
                    "end_time": my_timetable.end_time
                }
            }

            Studysession_list = load_records("studysession.json")
            Studysession_list.append(new_studysession)
            save_records("studysession.json", Studysession_list)

            add_studysession = input("Do you want to add more study sessions(Y/N): ")
            if add_studysession == "Y":
                continue
            else:
                break

    elif choice == "7":
        while True:
            attendance_id = StudentAttendance.generate_id()
            date = input("Enter the date(dd/mm/yyyy): ")
            student_id = input("Enter student id (s-000): ")
            timetable = input("Enter timetable: ")

            studentattendance = StudentAttendance(attendance_id, date, student_id, timetable)

            new_studentattendance = {
                "studentattendance": studentattendance.id,
                "date": studentattendance.date,
                "student_id": studentattendance.student_id,
                "timetable": studentattendance.timetable,
                "status": studentattendance.get_status()
            }

            StudentAttendance_list = load_records("studentattend.json")
            StudentAttendance_list.append(new_studentattendance)
            save_records("studentattend.json", StudentAttendance_list)

            add_studentattendance = input("Do you want to add more student attendance(Y/N): ")
            if add_studentattendance == "Y":
                continue
            else:
                break

    elif choice == "8":
        while True:
            lecturerattendance_id = LecturerAttendance.generate_id()
            date = input("Enter the date(dd/mm/yyyy): ")
            lecturer_id = input("Enter the lecturer id: ")

            lecturerattendance = LecturerAttendance(lecturerattendance_id, date, lecturer_id)

            new_lecturerattendance = {
                "lecturerattendance_id": lecturerattendance.id,
                "date": lecturerattendance.date,
                "lecturer_id": lecturerattendance.lecturer_id,
                "status": lecturerattendance.get_status()
            }

            LecturerAttendance_list = load_records("lecturerattend.json")
            LecturerAttendance_list.append(new_lecturerattendance)
            save_records("lecturerattend.json", LecturerAttendance_list)

            add_lecturerattendance = input("Do you want to add more lecturer attendances(Y/N): ")
            if add_lecturerattendance == "Y":
                continue
            else:
                break

    elif choice == "9":
        print("You have exited the program")
        break

    else:
        print("Invalid choice")
