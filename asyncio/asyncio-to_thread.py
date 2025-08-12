import asyncio
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

def block_long_running(limit:int):
    i = 1
    while i <= limit:
        time.sleep(1)
        log.info(f"wake up after 1 sec, count:{i}")
        i += 1

async def async_long_running(limit:int):
    i = 1
    while i <= limit:
        await asyncio.sleep(1)
        log.info(f"wake up after 1 sec, count:{i}")
        i += 1

async def main():
    coroutine1 = asyncio.to_thread(block_long_running,10)
    coroutine2 = asyncio.to_thread(block_long_running,10)
    coroutine3 = asyncio.to_thread(block_long_running,10)
    coroutine4 = async_long_running(10)


    await asyncio.gather(coroutine1,coroutine2,coroutine3,coroutine4)


if __name__ == "__main__":
    start_timestamp = time.perf_counter()
    asyncio.run(main())