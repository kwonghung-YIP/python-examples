def decorator(meth):
    def wrapper(self,*args,**kwargs):
        print(f"before invoke {self}.{meth}:")
        result = meth(self,*args,**kwargs)
        print(f"before invoke {self}.{meth}:result:{result}")
        return result
    return wrapper

class MyClass:
    def __init__(self,name):
        print("MyClass __init__")
        self.name

    @decorator
    def add(a.)
    