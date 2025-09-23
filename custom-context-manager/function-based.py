from contextlib import contextmanager
import time
import random

@contextmanager
def timer():
    print("start timer()...")
    startTime = time.perf_counter()
    print("timer() before yield")
    try:
        yield
        print("timer() after yield")
    except Exception as e:
        print("timer() exception after yield")
        print(f"captured exception: {type(e)}:{e}")
    finally:
        print("timer() finally...")
        endTime = time.perf_counter()
        elapse = endTime - startTime
        print(f"Elapse time:{elapse}")

if __name__ == "__main__":
    with timer() as t:
        x = sorted([random.randint(1,10000) for x in range(100000)])
        print(f"first(x):{x[0]}")
        print(f"last(x):{x[len(x)-1]}")
        y = 100/0