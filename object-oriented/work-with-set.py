class Employee:
    def __init__(self, id:str, name:str):
        self.__id = id
        self.name = name

    def __eq__(self, other):
        print("Employee __eq__")
        return isinstance(other,Employee) and self.__id == other.__id
        
    def __hash__(self):
        print("Employee __hash__")
        return hash(self.__id)
    
    def __repr__(self):
        return f"Employee:id:{self.__id},name:{self.name}"

if __name__ == "__main__":
    empA = Employee("a1234","Peter")
    #John has the same Id as Peter and will not be added into the set
    empB = Employee("a1234","John") 
    empC = Employee("A1231","Marry")

    print(f"{empA}:{hash(empA)}")
    print(f"{empB}:{hash(empB)}")
    print(f"{empC}:{hash(empC)}")
    print(empA==empB) 

    empSet = {empA,empB,empC,"hello",object(),(1,2,3)}    
    print(empSet)

