from enum import Enum

class Title(Enum):
    MR = "Mr"
    MRS = "Mrs"

class Person:
    email = "unknown"
    
    def __init__(self, firstName, lastName):
        self.title:Title = None
        self._firstName:str = firstName
        self._lastName:str = lastName

    def setTitle(self,title:Title):
        self.title = title

    def __str__(self) -> str:
        return f"name: {self.title.value} {self._firstName} {self._lastName} \
            email: {Person.email}"
    
