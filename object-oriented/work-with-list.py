from datetime import date

class Person:
    def __init__(self,name:str,dateOfBirth:date):
        self.name = name
        self.dateOfBirth = dateOfBirth

    def __lt__(self,other):
        print("Person __lt__ (operator <)")
        return isinstance(other,Person) and self.dateOfBirth < other.dateOfBirth

    def __le__(self,other):
        print("Person __lt__ (operator <=)")
        return isinstance(other,Person) and self.dateOfBirth <= other.dateOfBirth

    def __eq__(self,other):
        print("Person __lt__ (operator ==)")
        return isinstance(other,Person) and self.dateOfBirth == other.dateOfBirth

    def __ne__(self,other):
        print("Person __lt__ (operator !=)")
        return isinstance(other,Person) and self.dateOfBirth != other.dateOfBirth

    def __gt__(self,other):
        print("Person __lt__ (operator >)")
        return isinstance(other,Person) and self.dateOfBirth > other.dateOfBirth

    def __ge__(self,other):
        print("Person __lt__ (operator >=)")
        return isinstance(other,Person) and self.dateOfBirth >= other.dateOfBirth

if __name__ == "__main__":
    john = Person("John",date(1,1,1900))