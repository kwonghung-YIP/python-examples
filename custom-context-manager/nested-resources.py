import time


class ResourceA:
    def __init__(self):
        print("ResourceA __init__")

    def __enter__(self):
        print("ResourceA __enter__")
        self.name = "ResourceA"
        return self

    def __exit__(self,except_type,except_value,traceback):
        print("ResourceA __exit__")
        if except_type is not None:
            print(f"ResourceA catch exception:{except_type}-{except_value}")
            return True # ResourceA suppress the exception and won't propagate to ResourceB

class ResourceB:
    def __init__(self):
        print("ResourceB __init__")

    def __enter__(self):
        print("ResourceB __enter__")
        self.name = "ResourceB"
        return self

    def __exit__(self,except_type,except_value,traceback):
        print("ResourceB __exit__")
        if except_type is not None:
            print(f"ResourceB catch exception:{except_type}-{except_value}")


if __name__ == "__main__":
    with ResourceB() as b, ResourceA() as a:
        print("main...")
        print(f"{a.name},{b.name}")
        y = 100/0

    print("After with statement...")