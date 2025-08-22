import asyncio
import contextvars
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
context = contextvars.copy_context()

async def counting(condition:asyncio.Condition) -> None:
    try:
        log.info("waiting for acquiring the condition's lock...")
        async with condition:
            log.info("waiting for notification...")
            # release the lock and wait for notify() or notify_all()
            await condition.wait()
            # received notify() and acquire the lock again
            i = 1
            while i <= 5:
                await asyncio.sleep(1)
                cnt = counter.get()
                cnt += 1
                log.info(f"increasing counter by 1: {cnt}")
                counter.set(cnt)
                i += 1
            log.info("notify another task")
            condition.notify()
            log.info("complete and release condition's lock")
    except asyncio.CancelledError as err:
        log.info("catch asyncio.CancellerError")
        raise err

async def firstNotify(condition:asyncio.Condition, sleep) -> None:
    await asyncio.sleep(sleep)
    async with condition:
        log.info("notify another task...")
        condition.notify();    

async def main() -> None:
    condition = asyncio.Condition()
    awaitables = [asyncio.create_task(counting(condition),name=f"task-{i}",context=context) for i in range(1,11)]
    awaitables.append(firstNotify(condition,5))
    try:
        async with asyncio.timeout(30) as cm:
            await asyncio.gather(*awaitables)
    except TimeoutError:
        log.info("catch TimeoutError")
    log.info(f"main() completed")

if __name__ == "__main__":
    start_timestamp = time.perf_counter()
    asyncio.run(main())
    log.info(f"{__name__} completed")
