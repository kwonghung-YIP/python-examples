import time
import random

class Timer:
    def __init(self):
        print("Timer __init__")

    def __enter__(self):
        print("Timer __enter__")
        self.startTime = time.perf_counter()
        # return value to the target(s) specified in the as clause of the statement
        return self

    def __exit__(self, except_type, except_value, trace_back):
        print("Timer __exit__")
        if except_type is not None or except_value is not None:
            print(f"Exception captured in __exit__ {except_type}:{except_value}")
            return True # return True to suppress exception
        self.endTime = time.perf_counter()
        self.elapse = self.endTime - self.startTime
        print(f"Elapse time:{self.elapse}")

if __name__ == "__main__":
    with Timer() as timer:
        print(f"{timer.startTime}")
        x = sorted([random.randint(1,10000) for x in range(100000)])
        print(f"first(x):{x[0]}")
        print(f"last(x):{x[len(x)-1]}")
        y = 100/0
    
    print("After with statement...")