import time
import random

class Timer:
    def __init(self):
        print("Timer __init__")

    def __enter__(self):
        print("Timer __enter__")
        self.startTime = time.perf_counter()

    def __exit__(self, except_type, except_value, trace_back):
        print("Timer __exit__")
        print(f"Exception captured in __exit__ {except_type}:{except_value}")
        self.endTime = time.perf_counter()
        self.elapse = self.endTime - self.startTime
        print(f"Elapse time:{self.elapse}")

if __name__ == "__main__":
    with Timer() as timer:
        x = sorted([random.randint(1,10000) for x in range(100000)])
        print(f"first(x):{x[0]}")
        print(f"last(x):{x[len(x)-1]}")
        y = 100/0
    