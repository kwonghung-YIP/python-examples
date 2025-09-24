import asyncio
import time
import random

class AsyncTimer:
    def __init__(self):
        print("AsyncTimer __init__")

    async def __aenter__(self):
        print("AsyncTimer __aenter__")
        self.startTime = time.perf_counter()
        print("AsyncTimer __aenter sleep for 2 seconds...")
        await asyncio.sleep(2)
        return self

    async def __aexit__(self,except_type,except_value,traceback):
        print("AsyncTimer __aexit__")
        print("AsyncTimer __aexit sleep for 2 seconds...")
        await asyncio.sleep(2)
        self.endTime = time.perf_counter()
        self.elapse = self.endTime - self.startTime
        if not (except_type is None and except_value is None):
            print(f"Exception captured in __exit__ {except_type}:{except_value}")
            # return True to suppress exception, None is return by default to propagate the exception
            return True 

async def main():
    acm = AsyncTimer()
    async with acm as timer:
        print(f"main startTime:{timer.startTime}")
        print("main sleep for 2 seconds...")
        await asyncio.sleep(2)
        x = sorted([random.randint(1,10000) for x in range(100000)])
        print(f"first(x):{x[0]}")
        print(f"last(x):{x[len(x)-1]}")
        y = 100/0
    print(f"Elapse:{acm.elapse}")

if __name__ == "__main__":
    asyncio.run(main())