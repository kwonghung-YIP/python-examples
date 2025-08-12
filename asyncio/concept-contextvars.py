import asyncio
import contextvars
import random
import logging
import time

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

counter = contextvars.ContextVar("counter",default=0)

async def count_job(limit:int):
    i = 1
    sleepTtl = 0.0
    while i <= limit:
        cnt = counter.get()
        sleep = random.uniform(0.5,10)
        log.info(f"sleep for {sleep}, count: {cnt}")
        await asyncio.sleep(sleep)
        counter.set(cnt + 1)
        sleepTtl += sleep
        i += 1

    log.info(f"total sleep: {sleepTtl}, i: {i}")

async def main():
    coroutine1 = count_job(20)
    coroutine2 = count_job(20)
    coroutine3 = count_job(20)
    await asyncio.gather(coroutine1, coroutine2, coroutine3)
    log.info(f"counter: {counter.get()}")

    coroutine4 = count_job(30)
    coroutine5 = count_job(30)
    await asyncio.gather(coroutine4, coroutine5)

if __name__ == "__main__":
    start_timestamp = time.perf_counter()
    asyncio.run(main())