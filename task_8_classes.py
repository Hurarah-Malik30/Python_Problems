from typing import Union

class Student:
    def __init__(self,name:str,age:int,course:str):
        self.__name = name
        self.__age = age
        self.__course = course
    
    def getName(self) -> Union[None,str]:
        return self.__name

class Marks:
    def __init__(self,marks:int):
        self.marks = marks

    def getMarks(self):
        return self.marks

student_1 = Student('Ali',19,"Python")
marks_1 =  Marks(50)


print(isinstance(student_1, Student))
print(isinstance(marks_1, Student))
print(issubclass(Student, object))
print(issubclass(Marks, object))