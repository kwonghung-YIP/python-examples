def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"before invoke func{func}")
        result = func(*args,**kwargs)
        print(f"after invoke func:{func},result:{result}")
        return round(result,2)
    return wrapper

@decorator
def subtract(a:float,b:float) -> float:
    print(f"calling subtract:{a}-{b}")
    return a - b

if __name__ == "__main__":
    print(subtract(10,0.000001))
    print(subtract(10,b=0.000001))
    print(subtract(b=10,a=0.000001))