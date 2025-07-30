import time
import random
import logging
import asyncio

LOG_FORMAT = '%(asctime)s [%(levelname)s] %(message)s'
logging.basicConfig(format=LOG_FORMAT,level=logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
fmt = logging.Formatter(LOG_FORMAT)
ch.setFormatter(fmt)

log = logging.getLogger(__name__)
#log.addHandler(ch)

async def coroutine_without_await():
    print("hello!")

async def coroutine_with_await(caller,delay):
    print(f"hello {caller}...")
    await asyncio.sleep(delay)
    print("there!")

async def long_running_func(limit = 20):
    task = asyncio.current_task()
    tname = task.get_name()

    s = time.perf_counter()
    log.info("long_running_func[%s]: started...",tname)
    
    try:
        count:int = 1
        sleep_ttl:float = 0
        while count < limit:
            sleep:float = random.randint(1,10)
            sleep_ttl = sleep_ttl + sleep
            log.info("long_running_func[%s]: count %d, sleep for %d second...", tname, count, sleep)
            await asyncio.sleep(sleep)
            log.info("long_running_func[%s]: count %d, wake up after %d second", tname, count, sleep)
            count = count + 1
        log.info("long_running_func[%s]: exit after count %d", tname, count)
    except asyncio.CancelledError:
        log.info("long_running_func[%s]: cancelled",tname)
    finally:
        elapsed = time.perf_counter() - s
        log.info("long_running_func[%s]: completed, elapse: %d total sleep: %d",tname,elapsed,sleep_ttl)
        return count

async def cancel_tasks(*tasks:asyncio.Task):
    try:
        log.info("num of tasks: [%s]",len(tasks))
        await asyncio.sleep(30)
        log.info("wake up and start cancel tasks...")
        for t in tasks:
            log.info("Cancel task:[%s]",t.get_name())
            t.cancel()
    except asyncio.CancelledError:
        log.info("cancel cancel")

async def raise_exception_after(sleep:int):
    await asyncio.sleep(sleep)
    raise Exception("raise exception after %d seconds",sleep)

async def run_tasks():
    task = asyncio.create_task(coroutine_with_await("task",3))
    await task

async def run_gather():
    await asyncio.gather(coroutine_with_await("coroute",2),run_tasks())

def main1():
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

async def main2():
    task1 = asyncio.create_task(long_running_func(),name="Task1")
    task2 = asyncio.create_task(long_running_func(),name="Task2")
    task3 = asyncio.create_task(long_running_func(),name="Task3")
    cancelTask = asyncio.create_task(cancel_tasks(task1,task2,task3),name="cancelTask")

    await asyncio.gather(task1,task2,task3,cancelTask)

async def main3():
    try:
        async with asyncio.TaskGroup() as taskgrp:
            t1 = taskgrp.create_task(long_running_func(),name="GrpTask1")
            t2 = taskgrp.create_task(long_running_func(),name="GrpTask2")
            t3 = taskgrp.create_task(long_running_func(),name="GrpTask3")
            cancelTask = taskgrp.create_task(raise_exception_after(30),name="cancelTask")
    except Exception as e:
        log.info(f"Exception from task: {e}")
    finally:
        log.info("Counts t1:%s, t2:%s, t3:%s",t1.result(),t2.result(),t3.result())
        log.info("TaskGroup completed.")

if __name__ == "__main__":
    log.info(f"start {__name__} ...")
    s = time.perf_counter()

    #main1()
    asyncio.run(main3())

    elapsed = time.perf_counter() - s
    log.info(f"{__file__} executed in {elapsed} seconds.")
    log.info(f"finish {__name__} ...")
