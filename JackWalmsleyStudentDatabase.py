students = []


class StudentNotFoundException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        if self.message:
            return self.message
        else:
            return "No student by that description in database"

    pass


class Student:
    def __init__(self, first, last, number, average):
        self.first_name = first
        self.last_name = last
        self.student_number = number
        self.average = average
        students.append(self)

    @staticmethod
    def get_student_by_number(number):
        for s in students:
            if s.student_number == number:
                return s
        raise StudentNotFoundException("No student by that number in database")

    @staticmethod
    def get_students_by_first(first):
        result = []
        for s in students:
            if s.first_name == first:
                result.append(s)
        if len(result) == 0:
            raise StudentNotFoundException("No students with that first name in database")
        else:
            return result

    @staticmethod
    def get_board_average():
        return sum(s.average for s in students)


Student("Jeff", "Schust", 626689, 50)
print(Student.get_student_by_number(626689))
print(Student.get_students_by_first("Jeff"))
