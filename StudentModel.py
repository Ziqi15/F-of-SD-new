import random

class Student:
    def __init__(self, name, email, password):
        self.id = f"{random.randint(1, 999999):06d}"
        self.name = name
        self.email = email
        self.password = password
        self.subjects = []

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'subjects': self.subjects
        }

    @staticmethod
    def from_dict(data):
        student = Student(data['name'], data['email'], data['password'])
        student.id = data['id']
        student.subjects = data.get('subjects', [])
        return student
