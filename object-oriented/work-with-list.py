from datetime import date

class Person:
    def __init__(self,name:str,dateOfBirth:date):
        self.name = name
        self.dateOfBirth = dateOfBirth

    def __lt__(self,other):
        print("Person __lt__ (operator <)")
        return self.compareTo(other) > 0

    def __le__(self,other):
        print("Person __le__ (operator <=)")
        return self.compareTo(other) >= 0

    def __eq__(self,other):
        print("Person __eq__ (operator ==)")
        return self.compareTo(other) == 0

    def __ne__(self,other):
        print("Person __ne__ (operator !=)")
        return self.compareTo(other) != 0

    def __gt__(self,other):
        print("Person __gt__ (operator >)")
        return self.compareTo(other) < 0

    def __ge__(self,other):
        print("Person __ge__ (operator >=)")
        return self.compareTo(other) <= 0
    
    def __repr__(self):
        return f"{self.name}({self.dateOfBirth})"
    
    def compareTo(self,other) -> int:
        if (isinstance(other,Person)):
            if self.dateOfBirth == other.dateOfBirth:
                return 0 if self.name == other.name else 1 if self.name > other.name else -1
            else:
                return 1 if self.dateOfBirth > other.dateOfBirth else -1
        else:
            return -1 # Person instance comes first when comparing with other class

if __name__ == "__main__":
    john = Person("John",date(1900,1,31))
    peter = Person("Peter",date(1943,12,25))
    peter2 = Person("Peter",date(1943,12,25))
    mary = Person("Mary",date(1943,12,25))
    andy = Person("Andy",date(1989,6,4))

    print(andy < john) # T
    print(andy <= andy) # T
    print(peter == peter2) # T
    print(andy != john) # T
    print(mary > peter) # T
    print(mary >= mary) # T

    print(sorted([mary,john,peter,andy]))
    print([*reversed(sorted([mary,john,peter,andy]))])