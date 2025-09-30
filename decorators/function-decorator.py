def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"before invoke func{func}")
        try:
            result = func(*args,**kwargs)
            return round(result,2)
        finally:
            print(f"after invoke func:{func}")
    return wrapper

@decorator
def divide(a:float,b:float) -> float:
    print(f"calling divde:{a}/{b}")
    return a / b

def multiple(a:float,b:float) -> float:
    print(f"calling multiple:{a}/{b}")
    return a * b

multiple = decorator(multiple)

if __name__ == "__main__":
    print(divide(10,0.000001))
    print(divide(10,b=0.000001))
    print(divide(b=10,a=0.000001))
    print(multiple(3,4))
    print(divide(100,0))
    