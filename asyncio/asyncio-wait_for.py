import asyncio
import logging
import time

logging.basicConfig(level=logging.INFO)

log = logging.getLogger("asyncLogger")

async def running_for(seconds:float):
    try:
        log.info("start running_for")
        await asyncio.sleep(seconds)
        #time.sleep(seconds)
        log.info("complete running_for")
    except asyncio.CancelledError as err:
        # catch CancelledError if timeout before wakeup from sleep
        log.info("received CancelledError")
        # populate the CancelledError in order to raise 
        # the TimeoutError for asyncio.wait_for
        raise err

async def main():
    try:
        coroutine = running_for(30)
        task = asyncio.create_task(coroutine,name="mytask")
        await asyncio.wait_for(task,20)
    except TimeoutError as err:
        log.info("TimeoutError from asyncio.wait_for")

    log.info(f"task done? {task.done()}")
    for t in asyncio.all_tasks():
        log.info(f"{t} is not yet finished.")

if __name__ == "__main__":
    asyncio.run(main())