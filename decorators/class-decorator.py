def classDecorator(cls):
    @staticmethod
    def myFunc(a,b):
        return a + b
    cls.funcA = myFunc
    return cls

@classDecorator
class MyClass:
    def funcA(self,a,b):
        return a-b

def main():
    obj = MyClass()
    print(super(MyClass))
    print(f"{obj.funcA(4,5)}")

if __name__ == "__main__":
    main()
