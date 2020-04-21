# Name: Jack Walmsley
# Date: 2020-04-18
# Filename: JackWalmsleySQLStudentDatabase.py
# Purpose: To create a database of students while learning SQL
import sqlite3


class DuplicateStudentException(Exception):
    """
    Exception raised when a student is created that already exists
    """

    def __init__(self, message=None):
        self.message = message

    def __str__(self):
        if self.message:
            return self.message
        else:
            return "That student already exists"


class StudentNotFoundException(Exception):
    """
    Exception raised when a student can not be found with the provided information
    """

    def __init__(self, message=None):
        self.message = message

    def __str__(self):
        if self.message:
            return self.message
        else:
            return "No student by that description in database"


class Database:
    """
    A python wrapper for the SQL database, to avoid having to use SQL calls in the base code which tend to be lengthy
        and annoying
    """

    def __init__(self, filename: str):
        self.conn = sqlite3.connect(filename)
        self.c = self.conn.cursor()
        # Create the table if it doesn't already exist
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS students(number INTEGER PRIMARY KEY, firstname TEXT, lastname TEXT)''')

    def modify_student(self, number: int, firstname: str, lastname: str):
        """
        Modifies an existing student. If the student does not already exist, creates a new entry.
        Args:
            number: the number of the student
            firstname: the first name of the student
            lastname: the last name of the student
        """
        try:
            data = (number, firstname, lastname)
            self.c.execute('''REPLACE INTO students VALUES(?, ?, ?)''', data)
            self.conn.commit()
        except sqlite3.IntegrityError:
            raise DuplicateStudentException("A student with that number already exists")

    def delete_student(self, number: str):
        """
        Deletes a student from the database
        Args:
            number: the student number to remove from database
        """
        self.c.execute('''SELECT * FROM students WHERE number = ?''', (number,))
        if self.c.fetchone() is None:
            raise StudentNotFoundException
        self.c.execute('''DELETE FROM students WHERE number = ?''', (number,))
        self.conn.commit()

    def search_by_firstname(self, firstname: str):
        """
        Gets all students with specified first name
        Args:
            firstname: the first name of the students

        Returns:
            tuple: tuple of all students with the first name
        """
        self.c.execute('''SELECT * FROM students WHERE firstname = ?''', (firstname,))
        result = self.c.fetchall()
        if len(result) > 0:
            return result
        else:
            raise StudentNotFoundException

    def search_by_lastname(self, lastname: str):
        """
        Gets all students with specified last name
        Args:
            lastname: the last name of the students

        Returns:
            tuple: tuple of all students with the last name
        """
        self.c.execute('''SELECT * FROM students WHERE lastname = ?''', (lastname,))
        result = self.c.fetchall()
        if len(result) > 0:
            return result
        else:
            raise StudentNotFoundException

    def search_by_number(self, number: int):
        """
        Gets the student with specified number
        Args:
            number: the number of the student

        Returns:
            tuple: the tuple representation of a student
        """
        self.c.execute('''SELECT * FROM students WHERE number = ?''', (number,))
        result = self.c.fetchone()
        if result is not None:
            return result
        else:
            raise StudentNotFoundException

    def all_students(self):
        """
        Gets all students in database
        Returns:
            tuple: all students in tuple form (NUMBER, FIRST, LAST)

        """
        self.c.execute('''SELECT * FROM students''')
        return self.c.fetchall()


class UI:
    """
    The system for interfacing with the database
    """

    def __init__(self, db: Database):
        self.screens = {
            1: self.add,
            2: self.remove,
            3: self.display_all,
            4: self.search_database
        }
        self.db = db
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

    @staticmethod
    def result_to_text(result):
        """
        Converts the tuple returned by the database to a readable phrase
        Args:
            result (tuple): The tuple to convert to a string

        Returns:
            str:A readable version of result in form 'NUMBER, FIRST LAST

        """
        return "Number %d, %s %s" % (result[0], result[1], result[2])

    def add(self):
        """
        UI for adding students to the database
        """
        first = input("Enter the student's first name: ").capitalize()
        last = input("Enter the student's last name: ").capitalize()
        while True:
            num = input("Enter the student's number: ")
            try:
                num = int(num)
            except ValueError:
                print("Student number must be a number")
                continue
            break
        try:
            self.db.modify_student(num, first, last)
        except DuplicateStudentException as e:
            print(str(e))
        self.home()

    def remove(self):
        """
        UI for removing students from database
        """
        num = input("Enter the student number to be deleted: ")
        try:
            num = int(num)
            self.db.delete_student(num)
        except ValueError:
            print("Student number must be a number")
        except StudentNotFoundException as e:
            print(str(e))
        self.home()

    def display_all(self):
        """
        UI for displaying all students in database
        """
        all_students = self.db.all_students()
        if len(all_students) > 0:
            for s in all_students:
                print(self.result_to_text(s))
        else:
            print("No students in database")
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
            for s in self.db.search_by_firstname(first.capitalize()):
                print(self.result_to_text(s))
        except StudentNotFoundException as e:
            print(str(e))
        self.home()

    def search_by_last_name(self):
        """
        UI for searching the database by last name
        """
        last = input("Enter the student's last name': ")
        try:
            for s in self.db.search_by_lastname(last.capitalize()):
                print(self.result_to_text(s))
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
            print(self.result_to_text(self.db.search_by_number(num)))
        except ValueError:
            print("Student number must be a number")
        except StudentNotFoundException as e:
            print(str(e))
        self.home()


db = Database('students.db')

UI = UI(db)

UI.home()
