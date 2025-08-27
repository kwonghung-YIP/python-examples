import asyncio
import random
import time
import logging

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

async def countFor(barrier:asyncio.Barrier,cntFor:int) -> None:
    try:
        delay = random.randint(1,10)
        log.info(f"init delay for {delay} sec...")
        await asyncio.sleep(delay)
        log.info("waiting for barrier.wait()...")
        async with barrier:
            log.info(f"barrier released")
            i = 1
            while i <= cntFor:
                log.info(f"count:{i}")
                await asyncio.sleep(1)
                i += 1
        log.info("completed countFor()")
    except asyncio.CancelledError as err:
        log.info("catch asyncio.CancelledError")
        raise err
    
async def reporting(barrier:asyncio.Barrier) -> None:
    while True:
        log.info(barrier)
        await asyncio.sleep(1)

async def main() -> None:
    barrier = asyncio.Barrier(4)
    tasks = [ asyncio.create_task(countFor(barrier,10),name=f"task-{i}") for i in range(1,11) ]
    tasks.append(reporting(barrier))
    try:
        async with asyncio.timeout(22) as cm:
            await asyncio.gather(*tasks)
    except TimeoutError:
        log.info("catch TimeoutError")
    log.info("completed main()")

if __name__ == "__main__":
    start_timestamp = time.perf_counter()
    asyncio.run(main(),debug=True)
    log.info("completed __main__")