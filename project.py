from abc import ABC, abstractmethod
class Course:

    course = 0

    def __init__(self,course_id ,course_name, course_code, faculty):
        self.course_id = course_id
        self.course_name = course_name
        self.course_code = course_code
        self.faculty = faculty

    @classmethod
    def generate_id(cls):
        al = "C-"
        cls.course +=1
        return al + str(cls.course)

    def __str__(self):
        return f"{self.course_id} -{self.course_name} - {self.course_code} -({self.faculty})"

class Student:
    student = 0
    def __init__(self, student_id, first_name, last_name, faculty, contact, reg_no, year_of_study, gender, course):
    
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.faculty = faculty
        self.contact = contact
        self.email = self.get_email()
        self.reg_no = reg_no
        self.year_of_study = year_of_study
        self.gender = gender
        self.course = course

    @classmethod
    def generate_id(cls):
        st = "St-"
        cls.student +=1
        return st + str(cls.student)
    
    def get_email(self):
        self.email = f" {self.first_name}{self.last_name}@iuiu.ac"
        return self.email
        
        
    def __str__(self):
        return (
            f"{self.student_id} -> {self.first_name} -> {self.last_name} -> "
            f"{self.faculty} -> {self.contact} -> {self.email} -> {self.reg_no} -> "
            f"{self.year_of_study} -> {self.gender} -> {self.course}"
        )
    

class Lecturer:
    lecturer = 0
    def __init__(self, lecturer_id, first_name, last_name, faculty,gender,  contact,  department):
        self.lecturer_id = lecturer_id
        self.first_name = first_name
        self.last_name = last_name
        self.faculty = faculty
        self.gender = gender
        self.contact = contact
        self.email = self.get_email()
        self.department = department
    @classmethod
    def generate_id(cls):
        l = "Lec-"
        cls.lecturer +=1
        return l + str(cls.lecturer)
    
    def get_email(self):
        self.email = f" {self.first_name}{self.last_name}@iuiu.ac"
        return self.email
    
    def __str__(self):
        return f"{self.lecturer_id} -> {self.first_name} {self.last_name} -> {self.faculty} ->{self.gender} -> {self.contact} -> {self.email} ->{self.department} "
    

    

class CourseUnit:
    courseunit = 0
    def __init__(self,courseunit_id, courseunit_name, courseunit_code, course, credit_units):
        self.corseunit_id = courseunit_id
        self.courseunit_name = courseunit_name
        self.courseunit_code = courseunit_code
        self.course = course
        self.credit_units = credit_units

    @classmethod
    def generate_id(cls):
        cu = "CU-"
        cls.courseunit +=1
        return cu + str(cls.courseunit)
    
    def __str__(self):
        return f"{self.courseunit_name} ({self.courseunit_code})"
    
    
class Timetable:
    timetable = 0
    def __init__(self, session, day, course_unit, lecturer, start_time, end_time):
        self.session = session
        self.day = day
        self.course_unit = course_unit
        self.lecturer = lecturer
        self.start_time = start_time
        self.end_time = end_time
    @classmethod
    def generate_id(cls):
        tt= "Timetable-"
        cls.timetable +=1
        return tt + str(cls.timetable)
    
    def __str__(self):
        return (
            f"{self.day} | {self.course_unit} | {self.lecturer} | "
            f"{self.start_time} - {self.end_time}"
        )



class Attendance(ABC):
    def __init__(self,id, date, ):
        self.id = id
        self.date = date
        self.__status = "Present"
    def get_status(self):
        return self.__status

    @property
    def update_status(self, value):
        if value in ["Present", "Absent"]:
            self.status = value
        else:
            print("Invalid option")

    def __str__(self):
        return f"{self.id} -> {self.date} -> {self.get_status()}"
    
class StudentAttendance(Attendance):
    studentattendance = 0

    def __init__(self, id, date,  student_id, timetable,attendance_marks):
        super(). __init__(id , date)
        self.student_id = student_id
        self.timetable = timetable
        self.__status = "Present"
        self.attendance_marks = attendance_marks
    @classmethod
    def generate_id(cls):
        sa = "SA-"
        cls.studentattendance +=1
        return sa + str(cls.studentattendance)
    
    def get_status(self):
        return self.__status
    
                
    def __str__(self):
        return f"{self.id} -> {self.date}  -> {self.student_id} -> {self.get_status()} "
    
class LecturerAttendance(Attendance):
    lecturerattendance = 0

    def __init__(self, id ,date,  lecturer_id):
        super(). __init__(id, date)
        self.lecturer_id = lecturer_id
        self.__status = "Present"

    @classmethod
    def generate_id(cls):
        la = "LA-"
        cls.lecturerattendance +=1
        return la + str(cls.lecturerattendance)
          
        
    def __str__(self):
        return f"{self.id} -> {self.date} -> {self.lecturer_id} -> {self.get_status()}"
        
    

class Studysession:
    studysession = 0

    def __init__(self, study_session_id, academic_year, semester):
        self.study_session_id = study_session_id
        self.academic_year = academic_year
        self.semester = semester

        
    @classmethod
    def generate_id(cls):
        s = "SS-"
        cls.studysession +=1
        return s + str(cls.studysession)
        

    def __str__(self):
        return f"{self.academic_year} - {self.semester} - {self.get_status()}"

    


        