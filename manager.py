import json
from student import Student
class StudentManager:
    def __init__(self):
        self.students:list[Student]=[]

    def add_student(self,student:Student):
        self.students.append(student)

    def view_students(self):
        if not self.students:
            print("Students not found")
        else:
          for student in self.students:
            student.display()

    def search_student(self,student_id):
        for student in self.students:
            if student.student_id==student_id:
                return student
            
        return None

    def update_student(self, student_id):
        student=self.search_student(student_id)
        if student:
            name=input("Enter updated name: ")
            age=int(input("Enter new age: "))
            department=input("Enter new department: ")
            marks=int(input("Enter updated marks: "))
            student.name=name
            student.age=age
            student.department=department
            student.marks=marks
            student.grade=student.calculate_grade()
            print("Student updated successfully")
        else:
            print("Student not found.")

    def delete_student(self, student_id):
        student=self.search_student(student_id)
        if student:
            self.students.remove(student)
            print(f"The student {student.name} removed successfully")
        else:
            print("Student not found")

    def save_data(self, filename:str):
        data=[]
        for student in self.students:
            data.append(student.to_dict())

        with open(filename,"w") as file:
            json.dump(data,file,indent=4)

        print(f"Student data saved successfully to '{filename}'.")

    def load_data(self, filename:str):
        try:
            with open(filename,"r") as file:
                data=json.load(file)

            self.students.clear()


            for item in data:
                student=Student(
                 item["student_id"],
                 item["name"],
                 item["age"],
                 item["department"],
                 item["marks"]
                )
                self.students.append(student)
            print(f"Student data loaded successfully from '{filename}'.")

        except FileNotFoundError:
            print("File not found")

        except json.JSONDecodeError:
            print("Error reading json file")


