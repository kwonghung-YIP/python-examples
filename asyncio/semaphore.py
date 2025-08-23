import asyncio
import logging
import time
import random

start_timestamp: float

def add_elapse_time(record:logging.LogRecord) -> bool:
    record.elapse = time.perf_counter() - start_timestamp
    return True

LOG_FORMAT = '%(asctime)s [%(levelname)s] : %(message)s'
TASK_LOG_FORMAT = '%(asctime)s [%(levelname)s]|%(threadName)s|%(taskName)s|%(elapse)6.3f|%(funcName)s : %(message)s'
logging.basicConfig(format=LOG_FORMAT,level=logging.DEBUG)

formatter = logging.Formatter(fmt=TASK_LOG_FORMAT)

handler = logging.StreamHandler()
handler.setFormatter(formatter)
handler.addFilter(add_elapse_time)

log = logging.getLogger(__name__)
log.propagate = False
log.addHandler(handler)

async def countFor(semaphore:asyncio.Semaphore,cntFor:int) -> None:
    try:
        delay = random.randint(1,10)
        log.info(f"init delay for {delay} sec...")
        await asyncio.sleep(delay)
        log.info("waiting for others to release semaphore...")
        async with semaphore:
            log.info("acquire semaphore")
            i = 1
            while i <= cntFor:
                log.info(f"count:{i}")
                await asyncio.sleep(1)      
                i += 1
        log.info("completed counting().")
    except asyncio.CancelledError as err:
        log.info("catch asyncio.CancelledError")
        raise err
    
async def main() -> None:
    semaphore = asyncio.Semaphore(2)
    tasks = [ asyncio.create_task(countFor(semaphore,15),name=f"task-{i}") for i in range(1,11) ]
    try:
        async with asyncio.timeout(60) as cm:
            await asyncio.gather(*tasks)
    except TimeoutError:
        log.info("catch TimeoutError")
    log.info("main() completed.")

if __name__ == "__main__":
    start_timestamp = time.perf_counter()
    asyncio.run(main())
    log.info("__main__ completed.")
