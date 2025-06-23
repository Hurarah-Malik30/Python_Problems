class Student:
    def __init__(self,name:str,age:int,course:str):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Name:",self.name,"\nAge:",self.age,"\nCourse:",self.course)

student_1 = Student('Ahmad',20,'CSS')
student_2 = Student('Wajdan',19,'OS')
student_1.display()
student_2.display()