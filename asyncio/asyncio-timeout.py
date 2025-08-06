import time
import logging
import asyncio

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


async def wakeup_after(sleep:float):
    try:
        log.info("sleep for %d...", sleep)
        await asyncio.sleep(sleep)
        log.info("wake up after %d.", sleep)
    except Exception as err:
        log.info("catch Exception: %d", err)
    finally:
        log.info("completed.")

async def main():
    try:
        timeout = 3
        task = asyncio.create_task(wakeup_after(10),name="task1")
        log.info("asyncio.timeout in %d sec...", timeout)
        async with asyncio.timeout(timeout):
            await task
    except asyncio.TimeoutError as err:
        log.info("catch TimeoutError %s",err)

    log.info("task done? %s", task.done())


if __name__ == "__main__":
    start_timestamp = time.perf_counter()
    log.info(f"start {__name__} ...")

    asyncio.run(main(), debug=True)

    log.info(f"{__file__} executed.")
