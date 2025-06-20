from typing import Union

class Student:
    def __init__(self,name:str,age:int,course:str):
        self.__name = name
        self.__age = age
        self.__course = course
    
    def getName(self) -> Union[None,str]:
        return self.__name

    def modifyattr(self,name:str,age:int,course:str):
        self.__name = name
        self.__age = age
        self.__course = course

    def __str__(self):
        return f"Name: {self.__name}, Age: {self.__age}, Course: {self.__course}"

student_1 = Student('Saad',19,'Java')
print(student_1)
student_1.modifyattr('Ahsan',20,'Ruby')
print(student_1)