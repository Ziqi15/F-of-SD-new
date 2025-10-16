from Database import Database
from Colors import  COLORS

class AdminSystem:
    def __init__(self):
        self.db = Database()

    def run(self):
        while True:

            choice = input(f"{COLORS['CYAN']}\tAdmin System: (c)hange, (e)nrol, (r)emove (s)how or X: ").lower()

            if choice == 's':
                self.show_all_students()
            elif choice == 'r':
                self.remove_student()
            elif choice == 'g':
                self.group_students()
            elif choice == 'p':
                self.partition_students()
            elif choice == 'c':
                self.clear_all_data()
            elif choice == 'x':
                break
            else:
                print("Invalid option.")

    def show_all_students(self):
        students = self.db.load_students()
        if not students:
            print("No students found.")
            return
        for s in students:
            print(f"ID: {s.id} | Name: {s.name} | Email: {s.email}")
            if s.subjects:
                for subj in s.subjects:
                    print(f"  - {subj['id']}: {subj['name']} | Mark: {subj['mark']} | Grade: {subj['grade']}")
            else:
                print("  No subjects enrolled.")

    def remove_student(self):
        student_id = input("Enter student ID to remove: ")
        students = self.db.load_students()
        updated_students = [s for s in students if s.id != student_id]
        if len(updated_students) == len(students):
            print("Student ID not found.")
        else:
            self.db.save_students(updated_students)
            print("Student removed.")

    def group_students(self):
        students = self.db.load_students()
        if not students:
            print("No students to group.")
            return
        grade_groups = {'HD': [], 'D': [], 'C': [], 'P': [], 'F': []}
        for s in students:
            for subj in s.subjects:
                grade_groups[subj['grade']].append((s.name, subj['name'], subj['mark']))

        for grade, entries in grade_groups.items():
            print(f"\nGrade: {grade}")
            for entry in entries:
                print(f"  Student: {entry[0]} | Subject: {entry[1]} | Mark: {entry[2]}")

    def partition_students(self):
        students = self.db.load_students()
        pass_list = []
        fail_list = []

        for s in students:
            if not s.subjects:
                continue
            avg = sum(subj['mark'] for subj in s.subjects) / len(s.subjects)
            if avg >= 50:
                pass_list.append((s.name, avg))
            else:
                fail_list.append((s.name, avg))

        print("\nPASS students:")
        for s in pass_list:
            print(f"  {s[0]} | Avg: {s[1]:.2f}")

        print("\nFAIL students:")
        for s in fail_list:
            print(f"  {s[0]} | Avg: {s[1]:.2f}")

    def clear_all_data(self):
        confirm = input("Are you sure you want to delete ALL student data? (yes/no): ")
        if confirm.lower() == 'yes':
            self.db.save_students([])
            print("All student data cleared.")
        else:
            print("Operation cancelled.")
