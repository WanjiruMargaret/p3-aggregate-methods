from datetime import datetime

class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []
        self._grades = {}  # enrollment -> grade dictionary

    def enroll(self, course):
        if isinstance(course, Course):
            enrollment = Enrollment(self, course)
            self._enrollments.append(enrollment)
            course.add_enrollment(enrollment)
            return enrollment
        else:
            raise TypeError("course must be an instance of Course")

    def get_enrollments(self):
        return self._enrollments.copy()

    # ✅ Aggregate: count of courses a student is in
    def course_count(self):
        return len(self._enrollments)

    # ✅ Aggregate: average grade
    def aggregate_average_grade(self):
        if not self._grades:
            return None
        total_grades = sum(self._grades.values())
        num_courses = len(self._grades)
        return total_grades / num_courses

    # helper: add a grade
    def add_grade(self, enrollment, grade):
        if enrollment in self._enrollments:
            self._grades[enrollment] = grade
        else:
            raise ValueError("Enrollment does not belong to this student")


class Course:
    def __init__(self, title):
        self.title = title
        self._enrollments = []

    def add_enrollment(self, enrollment):
        if isinstance(enrollment, Enrollment):
            self._enrollments.append(enrollment)
        else:
            raise TypeError("enrollment must be an instance of Enrollment")

    def get_enrollments(self):
        return self._enrollments.copy()

    # ✅ Aggregate: count of students in this course
    def student_count(self):
        return len(self._enrollments)


class Enrollment:
    all = []
    
    def __init__(self, student, course):
        if isinstance(student, Student) and isinstance(course, Course):
            self.student = student
            self.course = course
            self._enrollment_date = datetime.now()
            type(self).all.append(self)
        else:
            raise TypeError("Invalid types for student and/or course")

    def get_enrollment_date(self):
        return self._enrollment_date

    # ✅ Class-level aggregate
    @classmethod
    def aggregate_enrollments_per_day(cls):
        enrollment_count = {}
        for enrollment in cls.all:
            date = enrollment.get_enrollment_date().date()
            enrollment_count[date] = enrollment_count.get(date, 0) + 1
        return enrollment_count
