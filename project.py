
from abc import ABC, abstractmethod


class Course:
    course = 0

    def __init__(self, course_id, course_name, course_code, faculty):
        self.course_id = course_id
        self.course_name = course_name
        self.course_code = course_code
        self.faculty = faculty

    @classmethod
    def generate_id(cls):
        s = "C-"
        cls.course += 1
        return s + str(cls.course)

    def __str__(self):
        return f"{self.course_name} - {self.course_code} - {self.faculty}"


class CourseUnit:
    def __init__(self, courseunit_id, courseunit_name, courseunit_code, course, credit_units):
        self.courseunit_id = courseunit_id
        self.courseunit_name = courseunit_name
        self.courseunit_code = courseunit_code
        self.course = course
        self.credit_units = credit_units

    def __str__(self):
        return f"{self.courseunit_name} - {self.courseunit_code} - {self.credit_units}"


class Student:
    def __init__(self, student_id, first_name, last_name, contact, reg_no, year_of_study, gender, course):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.contact = contact
        self.reg_no = reg_no
        self.year_of_study = year_of_study
        self.gender = gender
        self.course = course

    def get_email(self):
        return f"{self.first_name.lower()}.{self.last_name.lower()}@university.ac.ug"

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.reg_no}"


class Lecturer:
    def __init__(self, lecturer_id, first_name, last_name, faculty, gender, contact, department):
        self.lecturer_id = lecturer_id
        self.first_name = first_name
        self.last_name = last_name
        self.faculty = faculty
        self.gender = gender
        self.contact = contact
        self.department = department

    def get_email(self):
        return f"{self.first_name.lower()}.{self.last_name.lower()}@university.ac.ug"

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.department}"


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
        s = "Timetable-"
        cls.timetable += 1
        return s + str(cls.timetable)

    def __str__(self):
        return f"{self.session} - {self.day} - {self.course_unit} - {self.lecturer} - {self.start_time} - {self.end_time}"


class Studysession:
    studysession = 0

    def __init__(self, study_session_id, academic_year, semester):
        self.study_session_id = study_session_id
        self.academic_year = academic_year
        self.semester = semester
        self.timetables = []

    @classmethod
    def generate_id(cls):
        s = "SS-"
        cls.studysession += 1
        return s + str(cls.studysession)

    def add_timetable(self, timetable):
        self.timetables.append(timetable)

    def load_timetables(self, timetable_list):
        for t in timetable_list:
            timetable = Timetable(
                t["session"],
                t["day"],
                t["course_unit"],
                t["lecturer"],
                t["start_time"],
                t["end_time"]
            )
            self.add_timetable(timetable)

    def get_timetables(self):
        timetable_list = []

        for t in self.timetables:
            new_timetable = {
                "session": t.session,
                "day": t.day,
                "course_unit": t.course_unit,
                "lecturer": t.lecturer,
                "start_time": t.start_time,
                "end_time": t.end_time
            }
            timetable_list.append(new_timetable)

        return timetable_list

    def __str__(self):
        return f"{self.academic_year} - {self.semester}"

    def display_timetables(self):
        for timetable in self.timetables:
            print(timetable)


class Attendance(ABC):
    def __init__(self, id, date):
        self.id = id
        self.date = date
        self._status = 1

    @property
    def get_status(self):
        return self._status

    @abstractmethod
    def __str__(self):
        pass


class StudentAttendance(Attendance):
    def __init__(self, id, date, student):
        super().__init__(id, date)
        self.student = student

    def get_status(self):
        return self._status

    def __str__(self):
        return f"{self.student} - {self.date} - {self.get_status()}"


class LecturerAttendance(Attendance):
    def __init__(self, id, date, lecturer):
        super().__init__(id, date)
        self.lecturer = lecturer

    def get_status(self):
        return self._status

    def __str__(self):
        return f"{self.lecturer} - {self.date} - {self.get_status()}"
