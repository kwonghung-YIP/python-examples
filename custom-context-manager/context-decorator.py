import contextlib

class myContextDecorator(contextlib.ContextDecorator):
    def __init__(self):
        print("myContextDecorator __init__")
        self.name = "myContextDecorator"

    def __enter__(self):
        print("myContextDecorator __enter__")
        return self
    
    def __exit__(self, except_type, except_value, traceBack):
        print("myContextDecorator __exit__")
        if except_type is not None:
            print(f"myContextDecorator catch exception:{except_type}-{except_value}")
            return True # suppress exception

@myContextDecorator()
def funcA():
    print("in funcA")
    y = 100/0

if __name__ == "__main__":
    funcA()
    print("after funcA()...")