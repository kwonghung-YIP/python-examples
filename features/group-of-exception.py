import sys

def handle_group_exception(func,*args,**kwargs):
    try:
        print("try...")
        func(*args,**kwargs)
    except* ZeroDivisionError as exceptionGroup:
        print("found ZeroDivisionError in a error group")
        for err in exceptionGroup.exceptions:
            print(repr(err))

    except* TypeError as exceptionGroup:
        print("catch TypeError in a error group")
        for err in exceptionGroup.exceptions:
            print(repr(err))

    # catch general Excetpion at last to capture all others
    #except* Exception as exceptionGroup:
    #    print("catch General Exception in a error group")
    #    for err in exceptionGroup.exceptions:
    #        print(repr(err))

    finally:
        print("try-finally...")

def raiseGroupException():
    raise BaseExceptionGroup("group#1",[
        ZeroDivisionError("A"),TypeError("B"),
        BaseExceptionGroup("group#2",[
            ZeroDivisionError("C"),TypeError("D"),
        ]),
        RuntimeError('E')
    ])

def main():
    try:
        handle_group_exception(raiseGroupException)
    except ExceptionGroup as e:
        print(f"{type(e)}")
        for err in e.exceptions:
            print(f"{repr(err)}")

if __name__ == "__main__":
    main()