import asyncio
import logging
import random

logging.basicConfig(level=logging.INFO)

log = logging.getLogger("asyncLogger")

async def sleepAndRun(maxSleep:float):
    task = asyncio.current_task()
    try:
        sleep = round(random.uniform(0,maxSleep),4)
        log.info("sleep for %f seconds...",sleep)
        await asyncio.sleep(sleep)
        return f"{task.get_name()} completed after {sleep} secs!"
    except asyncio.CancelledError as err:
        log.info(f"{task.get_name()} catch CancelledError")
        raise err

async def main():
    coroutines = [sleepAndRun(30) for i in range(1,11)]
    for result in asyncio.as_completed(coroutines,timeout=25):
        try:
            msg = await result
            log.info(msg)
        except TimeoutError as err:
            log.info("catch TimeoutError from asyncio.as_completed")

if __name__ == "__main__":
    asyncio.run(main())