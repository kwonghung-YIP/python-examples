import contextlib
import asyncio
import time
import random


@contextlib.asynccontextmanager
async def asyncTimer():
    print("asyncTimer() start...")
    resource = {}
    resource['startTime'] = time.perf_counter()
    print("asyncTimer() sleep for 2 seconds before yield...")
    await asyncio.sleep(2)
    try:
        yield resource
    finally:
        print("asyncTimer() sleep for 2 seconds after yield...")
        await asyncio.sleep(2)
        resource['endTime'] = time.perf_counter()
        resource['elapse'] = resource['endTime'] - resource['startTime']
        print(f"Elapse time:{resource['elapse']}")

@asyncTimer()
async def main_decorator():
    #print(f"main() startTime:{t['startTime']}")
    print("sleep for 2 seconds in main...")
    await asyncio.sleep(2)
    x = sorted([random.randint(1,10000) for x in range(100000)])
    print(f"first(x):{x[0]}")
    print(f"last(x):{x[len(x)-1]}")

async def main_async_with():
    async with asyncTimer() as t:
        print(f"main() startTime:{t['startTime']}")
        print("sleep for 2 seconds in main...")
        await asyncio.sleep(2)
        x = sorted([random.randint(1,10000) for x in range(100000)])
        print(f"first(x):{x[0]}")
        print(f"last(x):{x[len(x)-1]}")
        y = 100/0
    
    print("After with statement")


if __name__ == "__main__":
    asyncio.run(main_decorator())
    asyncio.run(main_async_with())