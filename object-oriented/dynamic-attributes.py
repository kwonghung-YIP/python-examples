class DynaClass:
    def __init__(self,**attributes):
        print("DynaClass __init__")
        self.__attributeList = set()
        for name,value in attributes.items():
            self.__attributeList.add(name)
            setattr(self,name,value)

    def __getattribute__(self, name):
        print(f"DynaClass __getattribute__ {name}")
        # raise AttributeError if the "name" attribute does not exist,
        # and will fallback to __getattr__ if it is defined
        return super().__getattribute__(name)

    def __getattr__(self, name):
        print(f"DynaClass __getattr__ {name}")
        return super().__getattr__(self,name)

    def __setattr__(self, name, newValue):
        origValue = getattr(self,name) if hasattr(self,name) else None
        print(f"DynaClass __setattr__ {name}:[orig:{origValue},new:{newValue}]")
        super().__setattr__(name,newValue)
        if not name.startswith("_DynaClass_"):
            self.__attributeList.add(name)

    def __delattr__(self, name):
        origValue = getattr(self,name) if hasattr(self,name) else None
        print(f"DynaClass __delattr__ {name}:[orig:{origValue}]")
        super().__delattr__(name)
        self.__attributeList.remove(name)
    
    def __dir__(self):
        print(f"DynaClass __dir__")
        return self.__attributeList

    def __repr__(self):
        result = [ f"{name}=\"{getattr(self,name)}\"" for name in dir(self) if hasattr(self,name) ]
        return f"DynaClass({result})"

if __name__ == "__main__":
    obj1 = DynaClass(name="John Doe",salary=1000,dept="Eng")
    obj1.grade = "manager"
    obj1.salary = 1100
    print(obj1.name)
    print(obj1.salary)
    print(obj1.dept)
    print(obj1.grade)
    #print(obj1.unknown)
    del obj1.salary
    print(obj1)
    print(dir(obj1))

