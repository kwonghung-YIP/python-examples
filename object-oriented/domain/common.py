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
        self.__firstName:str = firstName
        self.__lastName:str = lastName

    #def __getattribute__(self, name):
    #    pass

    #def __setattr__(self, name, value):
    #    print(f"Person __setattr__ name:{name}, value:{value}")

    #def __delattr__(self, name):
    #    print(f"Person __delattr__ name:{name}")

    def __del__(self):
        print("Person __del__")

    def __str__(self) -> str: # informal
        print("Person __str__")
        return f"name: {self.title.value} {self.__firstName} {self.__lastName} \
            email: {Person.email}"

    def __repr__(self) -> str: # formal
        print("Person __repr__")
        return f"{self.__firstName} {self.__lastName}"

    def setTitle(self,title:Title):
        self.title = title

