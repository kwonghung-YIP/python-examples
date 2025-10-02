import sys

def try_except_finally(func,*args,**kwargs):
    """ doc statement for finally_return"""
    try:
        print("====")
        print("try...")
        result = func(*args,**kwargs)
        print(f"{repr(func)} result:{result}")
        print("last statement in try block")
    except ZeroDivisionError as err:
        print(f"catch ZeroDivisionError")
    except:
        exception = sys.exception()
        print(f"catch other exception {repr(exception)}")
    else:
        print("try-else without any exception")
    finally:
        print("try-finally...")

def finally_return(func,*args,**kwargs):
    """ doc statement for finally_return"""
    try:
        print("===")
        print("try...")
        result = func(*args,**kwargs)
        return result
    except (ZeroDivisionError,TypeError) as err:
        print(f"catch {repr(err)}...")
        return f"result after catched {repr(err)}"
    except:
        print(f"catch other exception {repr(sys.exception())}")
        return f"result after catched other exception"
    else:
        print(f"structurely unavailable try-else statement")
    finally:
        print("try-finally...")
        return "result from last return!"

def echo(name:str) -> str:
    return f"Hello {name.upper()}"

def raiseError(err):
    raise err

def main():
    try_except_finally(lambda a,b: a + b,5,6)
    try_except_finally(lambda a,b: a/b,b=0,a=100)
    try_except_finally(echo,123)

    print(finally_return(lambda: "I will be override!!!"))
    print(finally_return(lambda:100/0))
    print(finally_return(raiseError,TypeError("raise TypeError")))
    print(finally_return(raiseError,RuntimeError("raise RuntimeError")))

if __name__ == "__main__":
    main()