from contextlib import contextmanager
import time
import random

#
# Reference => https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager
#
@contextmanager
def timer():
    print("start timer()...")
    resource = {}
    resource['startTime'] = time.perf_counter()
    print("timer() before yield")
    try:
        yield resource # return resource to the target(s) specified in the as clause of the statement
        print("timer() after yield")
    except Exception as e:
        print("timer() exception after yield")
        print(f"captured exception: {type(e)}:{e}")
        raise e #propagate the exception
    finally:
        print("timer() finally...")
        resource['endTime'] = time.perf_counter()
        resource['elapse'] = resource['endTime'] - resource['startTime']
        print(f"Elapse time:{resource['elapse']}")

if __name__ == "__main__":
    with timer() as t:
        print(f"{t['startTime']}")
        x = sorted([random.randint(1,10000) for x in range(100000)])
        print(f"first(x):{x[0]}")
        print(f"last(x):{x[len(x)-1]}")
        y = 100/0

    print("After with statement...")