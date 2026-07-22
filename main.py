from student import Student
from manager import StudentManager

manager=StudentManager()

FileName="students.json"

while True:
    print("\n"+"="*40)
    print("      Student Management System")
    print("="*40)
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Save Data")
    print("7. Load Data")
    print("8. Exit")
    print("=" * 40)

    choice=input("Enter your choice: ")
    if choice=='1':
        student_id=input("Enter student Id: ")
        name=input("Enter name: ")
        age=int(input("Enter age: "))
        department=input("Enter department: ")
        marks=int(input("Enter marks: "))

        student=Student(student_id,name,age,department,marks)
        manager.add_student(student)

        print("Student added successfully")

    elif choice=='2':
        manager.view_students()

    elif choice=='3':
        student_id=input("Enter student ID: ")
        student=manager.search_student(student_id)
        if student:
            student.display()
        else:
            print("Student not found")
    elif choice=='4':
        student_id=input("Enter student Id to update: ")
        manager.update_student(student_id)

    elif choice == "5":
        student_id = input("Enter Student ID to delete: ")
        manager.delete_student(student_id)

    elif choice == "6":
        manager.save_data(FileName)

    elif choice == "7":
        manager.load_data(FileName)

    elif choice == "8":
        print("Thank you for using Student Management System.")
        break

    else:
        print("Invalid choice. Please try again.")