from enum import Enum

class Title(Enum):
    MR = "Mr"
    MRS = "Mrs"

class Person:
    email = "unknown"
    
    def __init__(self, firstName, lastName):
        self.title:Title = None
        self.firstName:str = firstName
        self.lastName:str = lastName

    def setTitle(self,title:Title):
        self.title = title

    def __str__(self) -> str:
        return f"name: {self.title.value} {self.firstName} {self.lastName} \
            email: {Person.email}"
    
