from enum import Enum

class Title(Enum):
    MR = "Mr"
    MRS = "Mrs"

class Person:
    email = "unknown"

    def __new__(cls, firstName, lastName):
        print("Person __new__")
        return super(Person,cls).__new__(cls)
    
    def __init__(self, firstName, lastName):
        print("Person __init__")
        self.title:Title = None
        self._firstName:str = firstName
        self._lastName:str = lastName

    #def __getattribute__(self, name):
    #    pass

    #def __setattr__(self, name, value):
    #    print(f"Person __setattr__ name:{name}, value:{value}")

    #def __delattr__(self, name):
    #    print(f"Person __delattr__ name:{name}")

    def __del__(self):
        print("Person __del__")

    def setTitle(self,title:Title):
        self.title = title

    def __str__(self) -> str:
        return f"name: {self.title.value} {self._firstName} {self._lastName} \
            email: {Person.email}"
    
