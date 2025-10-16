from StudentSystem import StudentSystem
from AdminSystem import AdminSystem
from Colors import  COLORS

def main():
    student_system = StudentSystem()
    admin_system = AdminSystem()

    while True:
        option = input(f"{COLORS['CYAN']}University System: (A)dmin, (S)tudent, or X: ")
        if option == "A":
            admin_system.run()
        elif option == "S":
            student_system.run()
        elif option == "X":
            print(f"{COLORS['YELLOW']}Thank you")
            return
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main()
    # Testing
