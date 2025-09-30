def decorator(meth):
    def wrapper(self,*args,**kwargs):
        print(f"before invoke {self.__class__.__name__}.{meth.__name__}")
        if (isinstance(self,MyClass) and meth.__name__=="follow"):
            if self.name == "John" and args[0] == "Peter":
                raise RuntimeError("John cannot follow Peter")
        try:
            result = meth(self,*args,**kwargs)
            return result
        finally:
            print(f"after invoke {self.__class__.__name__}.{meth.__name__}")
    return wrapper

class MyClass:
    def __init__(self,name):
        print("MyClass __init__")
        self.name = name

    @decorator
    def follow(self, user:str) -> bool:
        print(f"{self.name} follow {user}")
        return True
    
if __name__ == "__main__":
    john = MyClass("John")
    john.follow("Mary")
    john.follow("Peter")