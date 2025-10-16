import re
from StudentModel import Student
from Database import Database
from EnrollmentSystem import SubjectEnrolmentSystem
from Colors import  COLORS

class StudentSystem:
    def __init__(self):
        self.db = Database()

    def run(self):
        while True:

            choice = input(f"{COLORS['CYAN']}\tStudent System: (l)ogin, (r)egister, or X: ").lower()

            if choice == 'l':
                self.login()
            elif choice == 'r':
                self.register()
            elif choice == 'x':
                break
            else:
                print("Invalid option.")

    def register(self):
        name = input("Enter name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")

        if not self.validate_email(email):
            print("Invalid email format.")
            return

        if not self.validate_password(password):
            print("Password format incorrect.")
            return

        if self.db.find_student(email):
            print("Student already exists.")
            return

        student = Student(name, email, password)
        self.db.add_student(student)
        print(f"Registration successful! Your ID is {student.id}")

        print(f"{COLORS['YELLOW']}\temail and password formats acceptable{COLORS['RESET']}")

        # Step 3: Check if student exists
        if self.db.find_student(email):
            name_guess = email.split("@")[0].replace(".", " ").title()
            print(f"{COLORS['RED']}\tStudent {name_guess} already exists{COLORS['RESET']}")
            return

        # Step 4: Now ask for name
        name = input("\tEnter name: ")

        # Step 5: Create student
        student = Student(name, email, password)
        self.db.add_student(student)

        print(f"{COLORS['YELLOW']}E\tnrolling Student {student.name}{COLORS['RESET']}")


    def login(self):
        email = input("Enter email: ")
        password = input("Enter password: ")

        student = self.db.find_student(email, password)
        if student:
            print(f"Welcome, {student.name}!")
            print(f"Your ID is {student.id}")
                # 加入这行调用选课系统
            SubjectEnrolmentSystem(student).run()
        else:
             print("Invalid credentials.")

        student = self.db.find_student(email, password)
        if student:
            print(f"Welcome, {student.name}!")
            print(f"Your ID is {student.id}")
            print("You would now enter the subject enrolment menu...")
        else:
            print("Invalid credentials.")

    def validate_email(self, email):
        return re.fullmatch(r'[a-z]+\.[a-z]+@university\.com', email)

    def validate_password(self, password):
        return re.fullmatch(r'[A-Z][a-zA-Z]{4,}[0-9]{3,}', password)
