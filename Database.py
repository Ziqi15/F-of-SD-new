import os
import json
from StudentModel import Student

class Database:
    def __init__(self, filepath='students.data'):
        self.filepath = filepath
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w') as f:
                json.dump([], f)

    def load_students(self):
        with open(self.filepath, 'r') as f:
            return [Student.from_dict(data) for data in json.load(f)]

    def save_students(self, students):
        with open(self.filepath, 'w') as f:
            json.dump([s.to_dict() for s in students], f, indent=4)

    def add_student(self, student):
        students = self.load_students()
        students.append(student)
        self.save_students(students)

    def find_student(self, email, password=None):
        students = self.load_students()
        for s in students:
            if s.email == email and (password is None or s.password == password):
                return s
        return None

    def update_student(self, updated_student):
        students = self.load_students()
        for idx, s in enumerate(students):
            if s.email == updated_student.email:
                students[idx] = updated_student
                break
        self.save_students(students)
