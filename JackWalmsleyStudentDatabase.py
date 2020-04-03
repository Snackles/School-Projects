# Name: Jack Walmsley
# Date: 2020-03-09
# Filename: JackWalmsleyStudentDatabase.py
# Purpose: To create a searchable, modifiable database of students that is easy to interface with

students = []  # The database of students


class StudentNotFoundException(Exception):
    """
    Exception raised when a student can not be found with the provided information
    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        if self.message:
            return self.message
        else:
            return "No student by that description in database"


class DuplicateStudentException(Exception):
    """
    Exception raised when a student is created that already exists
    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        if self.message:
            return self.message
        else:
            return "That student already exists"


class Student:
    """
    The datatype for one student in the database
    """

    def __init__(self, first, last, number):
        self.first_name = first.capitalize()
        self.last_name = last.capitalize()
        self.student_number = number
        for s in students:
            if s.student_number == self.student_number:
                raise DuplicateStudentException("A student with that number already exists")
        students.append(self)

    def __str__(self):
        """
        Serializes the student object to a readable string
        :return: The student information in string format FIRST_NAME LAST_NAME, STUDENT_NUMBER
        """
        return self.first_name + " " + self.last_name + ",  " + str(self.student_number)

    def delete(self):
        """
        Removes the object from the database and frees up its memory
        """
        students.remove(self)
        del self

    @staticmethod
    def get_student_by_number(number):
        """
        Finds a student by student number
        :param number: the student number to search by
        :return: the student object with provided student number (there can only be one with any number)
        """
        for s in students:
            if s.student_number == number:
                return s
        raise StudentNotFoundException("No student by that number in database")

    @staticmethod
    def get_students_by_first_name(first):
        """
        Finds students by first name
        :param first: the first name to search for
        :return: a list of students with the provided first name
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
    def get_students_by_last_name(last):
        """
        Finds students by last name
        :param last: the last name to search for
        :return: a list of students with the provided last name
        """

        result = []
        for s in students:
            if s.last_name == last:
                result.append(s)
        if len(result) == 0:
            raise StudentNotFoundException("No students with that last name in database")
        else:
            return result


class UI:
    """
    The system for interfacing with the database
    """

    def __init__(self):
        self.screens = {
            1: self.add,
            2: self.remove,
            3: self.display_all,
            4: self.search_database
        }
        self.cursor_str = "> "  # The character to use as a cursor in the menus

    def home(self):
        """
        UI home screen
        """
        while True:
            print("1. Add Student")
            print("2. Remove Student")
            print("3. Display All Students")
            print("4. Search Database")
            user_choice = input(self.cursor_str)
            try:
                user_choice = int(user_choice)
                if user_choice not in self.screens:
                    raise ValueError
            except ValueError:
                print("Invalid choice. Try again")
                continue
            break
        self.screens[user_choice]()

    def add(self):
        """
        UI for adding students to the database
        """
        first = input("Enter the student's first name: ")
        last = input("Enter the student's last name: ")
        while True:
            num = input("Enter the student's number: ")
            try:
                num = int(num)
            except ValueError:
                print("Student number must be a number")
                continue
            break
        try:
            Student(first, last, num)
        except DuplicateStudentException as e:
            print(str(e))
        self.home()

    def remove(self):
        """
        UI for removing students from database
        """
        while True:
            num = input("Enter the student number to be deleted: ")
            try:
                num = int(num)
                Student.get_student_by_number(num).delete()
                break
            except ValueError:
                print("Student number must be a number")
                continue
            except StudentNotFoundException as e:
                print(str(e))
                continue
        self.home()

    def display_all(self):
        """
        UI for displaying all students in database
        """
        if len(students) == 0:
            print("No students in database")
        else:
            for s in students:
                print(s)
        self.home()

    def search_database(self):
        """
        UI home screen for searching the database
        """
        searches = {
            1: self.search_by_first_name,
            2: self.search_by_last_name,
            3: self.search_by_number,
        }
        print("1. Search by first name")
        print("2. Search by last name")
        print("3. Search by student number")
        user_choice = int(input(self.cursor_str))
        print(searches[user_choice]())

    def search_by_first_name(self):
        """
        UI for searching the database by first
        """
        first = input("Enter the student's first name': ")
        try:
            for s in Student.get_students_by_first_name(first.capitalize()):
                print(s)
        except StudentNotFoundException as e:
            print(str(e))
        self.home()

    def search_by_last_name(self):
        """
        UI for searching the database by last name
        """
        last = input("Enter the student's last name': ")
        try:
            for s in Student.get_students_by_last_name(last.capitalize()):
                print(s)
        except StudentNotFoundException as e:
            print(str(e))
        self.home()

    def search_by_number(self):
        """
        UI for searching the database by student number
        """
        num = input("Enter the student number to search: ")
        try:
            num = int(num)
            print(Student.get_student_by_number(num))
        except ValueError:
            print("Student number must be a number")
        except StudentNotFoundException as e:
            print(str(e))
        self.home()


UI = UI()

UI.home()
