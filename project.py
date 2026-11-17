
import json
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
    courseunit = 0

    def __init__(self, courseunit_id, courseunit_name, courseunit_code, course, credit_units):
        self.courseunit_id = courseunit_id
        self.courseunit_name = courseunit_name
        self.courseunit_code = courseunit_code
        self.course = course
        self.credit_units = credit_units

    @classmethod
    def generate_id(cls):
        s = "CU-"
        cls.courseunit += 1
        return s + str(cls.courseunit)

    def __str__(self):
        return f"{self.courseunit_name} - {self.courseunit_code} - {self.credit_units}"


class Student:
    student = 0

    def __init__(self, student_id, first_name, last_name, contact, reg_no, year_of_study, gender, course):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.contact = contact
        self.reg_no = reg_no
        self.year_of_study = year_of_study
        self.gender = gender
        self.course = course

    @classmethod
    def generate_id(cls):
        s = "S-"
        cls.student += 1
        return s + str(cls.student)

    def get_email(self):
        return f"{self.first_name.lower()}.{self.last_name.lower()}@university.ac.ug"

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.reg_no}"


class Lecturer:
    lecturer = 0

    def __init__(self, lecturer_id, first_name, last_name, faculty, gender, contact, department):
        self.lecturer_id = lecturer_id
        self.first_name = first_name
        self.last_name = last_name
        self.faculty = faculty
        self.gender = gender
        self.contact = contact
        self.department = department

    @classmethod
    def generate_id(cls):
        s = "L-"
        cls.lecturer += 1
        return s + str(cls.lecturer)

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
        self.timetables = []

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

    def save_timetables(self):
        with open("studysession.json", "r") as doc:
            Studysession_list = json.load(doc)

        found = False

        for session in Studysession_list:
            if session["study_session_id"] == self.study_session_id:
                session["timetables"] = self.get_timetables()
                found = True
                break

        if found:
            with open("studysession.json", "w") as doc:
                json.dump(Studysession_list, doc, indent=4)
            print("Timetable saved successfully!")
        else:
            print("Study session not found!")

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
    studentattendance = 0

    def __init__(self, id, date, student):
        super().__init__(id, date)
        self.student = student

    @classmethod
    def generate_id(cls):
        cls.studentattendance += 1
        return "SA-" + str(cls.studentattendance)

    def get_status(self):
        return self._status

    def __str__(self):
        return f"{self.student} - {self.date} - {self.get_status()}"


class LecturerAttendance(Attendance):
    lecturerattendance = 0

    def __init__(self, id, date, lecturer):
        super().__init__(id, date)
        self.lecturer = lecturer

    @classmethod
    def generate_id(cls):
        cls.lecturerattendance += 1
        return "LA-" + str(cls.lecturerattendance)

    def get_status(self):
        return self._status

    def __str__(self):
        return f"{self.lecturer} - {self.date} - {self.get_status()}"

