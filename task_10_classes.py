from typing import Union

class Student:
    def __init__(self,name:str,age:int,course:str):
        self.name = name
        self.age = age
        self.course = course
    
    def getName(self) -> Union[None,str]:
        return self.name

    def modifyattr(self,name:str,age:int,course:str):
        self.name = name
        self.age = age
        self.course = course

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Course: {self.course}"

student_ = Student('Wajdan',20,'LLB')
print("Simpele Class Attributes:")
print(student_)

student_.student_teacher = 'Usman Ghani'
print('After Adding student_teacher:')
for attr,value in student_.__dict__.items():
    if not attr.startswith('_'):
        print(f'{attr} -> {value}')

del student_.name
print('After Deleting name:')
for attr,value in student_.__dict__.items():
    if not attr.startswith('_'):
        print(f'{attr} -> {value}')