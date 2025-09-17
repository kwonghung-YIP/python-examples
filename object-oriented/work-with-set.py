class Employee:
    def __init__(self, id:str):
        self.__id = id

    def __eq__(self, other):
        print("Employee __eq__")
        return isinstance(other,Employee) and self.__id == other.__id
        
    def __hash__(self):
        print("Employee __hash__")
        return hash(self.__id)
    
    def __repr__(self):
        return f"Employee:{self.__id}"

if __name__ == "__main__":
    empA = Employee("a1234")
    empB = Employee("a1234") #empA and empB got the same id
    empC = Employee("A1231")

    empSet = {empA,empB,empC,"hello",object(),(1,2,3)}
    print(f"{empA}:{hash(empA)}")
    print(f"{empB}:{hash(empB)}")
    print(f"{empC}:{hash(empC)}") 
    
    print(empSet)

