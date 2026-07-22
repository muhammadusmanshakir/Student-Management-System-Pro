class Student:

    def __init__(self,student_id,name,age,department,marks):
        self.student_id=student_id
        self.name=name
        self.age=age
        self.department=department
        self.marks=marks
        self.grade=self.calculate_grade()

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >=80:
            return "B"
        elif self.marks >=70:
            return "C"
        elif self.marks >=60:
            return "D"
        else:
            return "F"
        
    def display(self):
        print("-"*40)
        print(f"Student ID: {self.student_id}")
        print(f"Name      : {self.name}")
        print(f"Age       : {self.age}")
        print(f"Department: {self.department}")
        print(f"Marks     : {self.marks}")
        print(f"Grade     : {self.grade}")

        print("-"*40)
        

    def to_dict(self):
     return{
        "student_id" : self.student_id,
        "name" :self.name,
        "age" : self.age,
        "department" : self.department,
        "marks" : self.marks,
        "grade" : self.grade
      }


