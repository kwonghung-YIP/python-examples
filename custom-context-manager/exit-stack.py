import contextlib

class MyResource:
    def __init__(self,name):
        print(f"MyResource __init__:{name}")
        self.name = name

    def __enter__(self):
        print(f"MyResource __enter__:{self.name}")
        return self
    
    def __exit__(self,except_type,except_value,traceback):
        print(f"MyResource __exit__:{self.name}")
        if except_type is not None:
            print(f"MyResource catch exception:{self.name}:{except_type}-{except_value}")

def callback(paramA,paramB):
    print(f"callback({paramA},{paramB})")

def main():
    with contextlib.ExitStack() as exitStack:
        resB = exitStack.enter_context(MyResource("resourceB"))
        resA = exitStack.enter_context(MyResource("resourceA"))
        resC = exitStack.enter_context(MyResource("resourceC"))

        # "push" only register the __exit__ function for resourceD
        # __enter__ function of resourceD has not been invoked
        resD = exitStack.push(MyResource("resourceD"))
        
        print(f"{resA.name},{resB.name},{resC.name},{resD.name}")
        
        # callbacks are invoked after completed the with block
        exitStack.callback(callback,"A","B")
        exitStack.callback(callback,"B","C")
        
        try:
            y = 100/0
        finally:
            print("last statement in with statement")
            # close() Immediately unwinds the callback stack
            # exitStack.close()

    print("After with statement...")

# expected callback and __exit__ sequence (last come first call)
#
# callback(B,C)
# callback(A,B)
# MyResource __exit__:resourceD
# MyResource catch exception:resourceD:<class 'ZeroDivisionError'>-division by zero
# MyResource __exit__:resourceC
# MyResource catch exception:resourceC:<class 'ZeroDivisionError'>-division by zero
# MyResource __exit__:resourceA
# MyResource catch exception:resourceA:<class 'ZeroDivisionError'>-division by zero
# MyResource __exit__:resourceB
# MyResource catch exception:resourceB:<class 'ZeroDivisionError'>-division by zero
# Traceback (most recent call last):
#  File "/home/hung/projects/python-spikes/custom-context-manager/exit-stack.py", line 54, in <module>
#    main()
#  File "/home/hung/projects/python-spikes/custom-context-manager/exit-stack.py", line 36, in main
#    y = 100/0
#        ~~~^~
# ZeroDivisionError: division by zero

if __name__ == "__main__":
    main()