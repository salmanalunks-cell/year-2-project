from project import Student, Lecturer, Course, CourseUnit, Studysession, Timetable, StudentAttendance, LecturerAttendance
import json


Course_list = []
Student_list = []
Lecturer_list = []
Courseunit_list = []
Timetable_list = []
Studysession_list = []
StudentAttendace_list = []
LecturerAttendance_list = []



while True:    
    print("\n1.Course registration\n2.Student Registration\n3.Lecturer Registration\n4.Add courseunits\n5.Timetable\n6.Student Attendance\n7.Study Session\n8.Lecturer Attendance\n9.Exit\n")
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
            with open("course.json", "r") as doc:
                Course_list = json.load(doc)
                
            with open("course.json", "w") as doc:
                Course_list.append(new_course)
                json.dump(Course_list, doc, indent=4)
                
            add_course = input("Do you have more courses to add (Y/N): ")
            if add_course == "Y":
                continue
            else:
                break
    
    
    elif choice == "2":
        while True:
    
            student_id = Student.generate_id()
            student_first_name = input("Enter student's first name: ")
            student_last_name = input("Enter student's last name : ")
            faculty = input("Enter faculty : ")
            contact = input("Enter student contact number: ")
            registration_number = input("Enter student registration number : ")
            year_of_study = input("Enter year of study: ")
            gender = input("Enter student gender: ")
            course = input("Enter the student's course: ")
            
        #instance
            student = Student(  student_id, student_first_name, student_last_name,faculty, contact, registration_number, year_of_study, gender , course) 
                               
            
            
            new_student ={
                "student_id" : student.student_id,
                "student_first_name" : student.first_name,
                "student_last_name" : student.last_name,
                "faculty" : student.faculty,
                "contact": student.contact,
                "registration_number" : student.reg_no,
                "year_of_study" : student.year_of_study,
                "gender": student.gender,
                "course": student.course,
                "email": student.get_email()
            }


            with open("student.json", "r") as doc:
                        Student_list = json.load(doc)
                    
            with open("student.json", "w") as doc:
                Student_list.append(new_student)
                json.dump(Student_list,doc, indent = 4)
            
            
                
            
                    
            add_student = input("Do you have more students to add (Y/N): ") 
            
            if add_student == "Y":
                continue
            else:
                break
             
        
    elif choice == "3":
        
        while True:
            lecturer_id = Lecturer.generate_id()
            lecturer_first_name = input("Enter Lecturer's first name: ")
            lecturer_last_name = input("Enter lecturer's last name: ")
            faculty = input("Enter the faculty: ")
            gender = input("Enter the gender: ")
            contact = input("Enter Lecturer's contact: ")
            department = input("Enter the department: ")
    #instance
            lecturer = Lecturer(lecturer_id, lecturer_first_name, lecturer_last_name, faculty, gender, contact, department  )
            
            new_lecturer = {
                
                "lecturer_id" : lecturer.lecturer_id,
                "lecturer_first_name" : lecturer.first_name,
                "lecturer_last_name" : lecturer.last_name,
                "faculty" : lecturer.faculty,
                "gender" :lecturer.gender,
                "contact" : lecturer.contact,
                "department" : lecturer.department,
                "email " :lecturer.get_email()
                
                
            }
            
            with open("lecturer.json", "r") as doc:
                Lecturer_list = json.load(doc)
                
            with open("lecturer.json", "w") as doc:
                Lecturer_list.append(new_lecturer)
                json.dump(Lecturer_list , doc , indent= 4)
            
            add_lecturer = input("Do you have more lecturers to add (Y/N): ")
            
            if add_lecturer == "Y":
                continue
            else:
                break
    
    elif choice == "4":
        while True:
            
            courseunit_id = CourseUnit.generate_id()
            courseunit_name = input("Enter course unit name : ")
            courseunit_code = input("Enter course unit code: ")
            course = input("Enter course: ")
            credit_units = input("Enter credit units: ")
         #instance
            
            courseunit = CourseUnit(courseunit_id, courseunit_name, courseunit_code, course, credit_units)
            
            new_courseunit = {
                "courseunit_id": courseunit.courseunit_id,
                "courseunit_name": courseunit.courseunit_name,
                "courseunit_code": courseunit.courseunit_code,
                "course": courseunit.course,
                "credit_units": courseunit.credit_units
            }
            
            with open ("courseunit.json", "r") as doc:
               Courseunit_list = json.load(doc)
               
            with open("courseunit.json", "w") as doc:
                Courseunit_list.append(new_courseunit)
                json.dump(Courseunit_list, doc, indent = 4)
                
            add_courseunit = input("Do you have more coursunits to add(Y/N): ")
            if add_courseunit == "Y":
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
            
            with open ("timetable.json", "r" ) as doc:
                Timetable_list = json.load(doc)
            
            Timetable_list.append(new_timetable)
            
            with open("timetable.json", "w") as doc:
                json.dump(Timetable_list, doc, indent = 4)
                
            add_timetable = input("Do you want to add more timetable(Y/N): ")
            if add_timetable == "Y":
                continue    
            else:
                break
            
    elif choice == "6":
        while True:
            
            studentattendance_id = StudentAttendance.generate_id()
            date = input("Enter the date(dd/mm/yyyy): ")
            student_id = input("Enter the student id number: ")
            timetable = input("Enter timetable : ")
            
            studentattendance = StudentAttendance(studentattendance_id, date, student_id, timetable)
            
            new_studentattendance ={
                "studentattendance": studentattendance.id,
                "date": studentattendance.date,
                "student_id": studentattendance.student_id,
                "timetable": studentattendance.timetable,
                "status": studentattendance.get_status(),

                
            }
            
            with open ("studentattend.json" , "r")as doc:
                StudentAttendance_list = json.load(doc)
                
            with open ("studentattend.json", "w")as doc:
                StudentAttendance_list.append(new_studentattendance)
                json.dump(StudentAttendance_list, doc, indent = 4)
                
            add_studentattendance = input("Do you want to add more student attendance(Y/N): ")
            if add_studentattendance == "Y":
                continue
            else:
                break   
            
            
    elif choice == "7":
        while True:
            
            study_session_id = Studysession.generate_id()
            academic_year = input("Enter the academic year: ")
            semester = input("Enter the semester: ")
            
        #instance
            studysession = Studysession(study_session_id, academic_year, semester)
            
            new_studysession ={
                "study_session_id": studysession.study_session_id,
                "academic_year": studysession.academic_year,
                "semester": studysession.semester,
                "status": studysession.get_status()
                
            }
            with open ("studysession.json", "r")as doc:
                Studysession_list = json.load(doc)
                
            with open ("studysession.json","w")as doc:
                Studysession_list.append(new_studysession)
                json.dump(Studysession_list,doc , indent = 4)
                
            add_studysession = input("Do you want to add more study sessions(Y/N): ")
            if add_studysession == "Y":
                continue
            else:
                break
            
    elif choice == "8":
        lecturerattendance_id = LecturerAttendance.generate_id()
        date = input("Enter the date(dd/mm/yyyy): ")
        lecturer_id = input ("Enter the lecturer id : ")
        
        lecturerattendance = LecturerAttendance(lecturerattendance_id, date, lecturer_id)
        
        new_lecturerattendance = {
            "lecturerattendance_id" : lecturerattendance.id,
            "date" : lecturerattendance.date,
            "lecturer_id" : lecturerattendance.lecturer_id,
            "status": lecturerattendance.get_status()
        }
        
        with open("lecturerattend.json", "r")as doc:
            LecturerAttendance_list = json.load(doc)
            
        with open("lecturerattend", "w")as doc:
            LecturerAttendance_list.append(new_lecturerattendance)
            json.dump( LecturerAttendance_list, doc, indent = 4)
            
            add_lecturerattendance = input("Do you want to add more lecturer attendances(Y/N): ")
            
            if add_lecturerattendance == "Y":
                continue
            else:
                break
    else:
        print("You have exited the program")
        break
        