from SubjectModel import Subject
from Database import Database

class SubjectEnrolmentSystem:
    def __init__(self, student):
        self.student = student
        self.db = Database()

    def run(self):
        while True:
            print(f"\n=== Subject Enrolment System for {self.student.name} ===")
            print("(c) Change password")
            print("(e) Enrol in a subject")
            print("(r) Remove a subject")
            print("(s) Show enrolled subjects")
            print("(x) Exit")

            choice = input("Enter choice: ").lower()
            if choice == 'c':
                self.change_password()
            elif choice == 'e':
                self.enrol_subject()
            elif choice == 'r':
                self.remove_subject()
            elif choice == 's':
                self.show_subjects()
            elif choice == 'x':
                self.db.update_student(self.student)
                break
            else:
                print("Invalid choice.")

    def change_password(self):
        new_pass = input("Enter new password: ")
        self.student.password = new_pass
        print("Password changed successfully.")

    def enrol_subject(self):
        if len(self.student.subjects) >= 4:
            print("You can't enrol in more than 4 subjects.")
            return
        name = input("Enter subject name to enrol: ")
        new_subject = Subject(name)
        self.student.subjects.append(new_subject.to_dict())
        print(f"Enrolled in {name} with ID {new_subject.id}, mark {new_subject.mark}, grade {new_subject.grade}")

    def remove_subject(self):
        if not self.student.subjects:
            print("No subjects to remove.")
            return
        self.show_subjects()
        subj_id = input("Enter subject ID to remove: ")
        original_len = len(self.student.subjects)
        self.student.subjects = [s for s in self.student.subjects if s['id'] != subj_id]
        if len(self.student.subjects) < original_len:
            print("Subject removed.")
        else:
            print("Subject ID not found.")

    def show_subjects(self):
        if not self.student.subjects:
            print("You have not enrolled in any subjects.")
            return
        total = 0
        print("\nEnrolled Subjects:")
        for s in self.student.subjects:
            print(f"- {s['id']}: {s['name']} | Mark: {s['mark']} | Grade: {s['grade']}")
            total += s['mark']
        avg = total / len(self.student.subjects)
        print(f"Average Mark: {avg:.2f}")
        print("Status:", "PASS" if avg >= 50 else "FAIL")
