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
    """
    The datatype for one student in the database
    """
    def __init__(self, first, last, number, average):
        self.first_name = first
        self.last_name = last
        self.student_number = number
        self.average = average
        students.append(self)

    def delete(self):
        students.remove(self)
        del self

    @staticmethod
    def get_student_by_number(number):
        """
        Finds a student by student number
        :param number: the student number to search by
        :return: the student object with provided student number
        """
        for s in students:
            if s.student_number == number:
                return s
        raise StudentNotFoundException("No student by that number in database")

    @staticmethod
    def get_students_by_first(first):
        """
        Finds students by first name
        :param first: the first name to search for
        :return: a list of student with the provided first name
        """
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
        """
        Finds the average of all student averages in the database
        :return: the average of all student averages
        """
        return sum(s.average for s in students)


Student("Jeff", "Schust", 626689, 50)
print(Student.get_student_by_number(626689))
print(Student.get_students_by_first("Jeff"))
