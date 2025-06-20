from typing import Union

class Greeting:
    
    def __init__(self,name):
        self.__name = name #__name specifies that it is a private attribute

    def sayhello(self) -> Union[None,str]: #Union[None,str] specifies which values the function can return
        print("hello,",self.name)

    @staticmethod
    def say_my_name(name:str) -> str:
        print(f"My name is {name}")

greeting_1 = Greeting("Munneb")
print(greeting_1.__dict__)