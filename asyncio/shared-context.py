import asyncio
import contextvars
import random

counter = contextvars.ContextVar('counter',default=0)
context = contextvars.copy_context()

async def counting(limit:int):
    i:int = 1
    while i <= limit:
        sleep:float = round(random.uniform(1,5),2)
        print(f"sleep for {sleep} sec")
        await asyncio.sleep(1)
        ctr = counter.get()
        print(f"increase counter from {ctr} by 1")
        ctr += 1
        counter.set(ctr)
        i += 1

async def main():
    task1 = asyncio.create_task(counting(5),context=context)
    task2 = asyncio.create_task(counting(5),context=context)

    await asyncio.gather(task1,task2)

    print(f"counter is {counter.get()}")

if __name__ == "__main__":
    asyncio.run(main())