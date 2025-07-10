import time
import random
import threading
import asyncio

from functools import reduce

counter:int = 0

async def count(id:str):
    s = time.perf_counter()
    invoke = 0;
    global counter
    while counter <= 500:
        invoke = invoke + 1
        counter = counter + 1
        print(f"func #{id} run on thread {threading.current_thread().name}")
        print(f"func #{id} increase counter to {counter}")
        sleep:int = random.randint(1,20)
        print(f"func #{id} sleep for {sleep} seconds")
        # await keyword pass control back to event-loop
        await asyncio.sleep(sleep)
    elapsed = time.perf_counter() - s
    print(f"func #{id} executed in {elapsed} seconds.")
    return invoke

async def gather():
    return await asyncio.gather(*(count(f"func#{i}") for i in range(100)))

if __name__ == "__main__":
    s = time.perf_counter()
    res = asyncio.run(gather())
    print(f"total # of invokes: {reduce(lambda a,b: a+b, res)}")
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed} seconds.")