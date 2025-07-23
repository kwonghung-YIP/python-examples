import time
import asyncio

async def coroutine_without_await():
    print("hello!")

async def coroutine_with_await(caller,delay):
    print(f"hello {caller}...")
    await asyncio.sleep(delay)
    print("there!")

async def run_tasks():
    task = asyncio.create_task(coroutine_with_await("task",3))
    await task

async def run_gather():
    await asyncio.gather(coroutine_with_await("coroute",2),run_tasks())

if __name__ == "__main__":
    s = time.perf_counter()

    # Type of coroutine function is a function
    print(f"type of \"coroutine_without_await\": {type(coroutine_without_await)}")
    print(f"type of \"coroutine_with_await\": {type(coroutine_with_await)}")

    coroutine_woa = coroutine_without_await()
    coroutine_wa = coroutine_with_await("coroutine",2)

    # Execute coroutineFunc() return a Coroutine instance
    print(f"type of \"coroutine_without_await\" instance: {type(coroutine_woa)}")
    print(f"type of \"coroutine_with_await\" instance: {type(coroutine_wa)}")

    # Run a coroutine instance with an event-loop
    asyncio.run(coroutine_woa)
    asyncio.run(coroutine_wa)
    asyncio.run(run_tasks())
    
    # cannot rerun completed coroutine
    try:
        asyncio.run(coroutine_woa)
    except RuntimeError as e:
        print(e)

    asyncio.run(run_gather())

    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed} seconds.")