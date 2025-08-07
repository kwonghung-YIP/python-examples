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
        timeout = 10
        task = asyncio.create_task(wakeup_after(60),name="task1")
        async with asyncio.timeout(timeout) as contextManager:
            log.info("current deadline is %d seconds...", contextManager.when())
            log.info("sleep for %d seconds",3)
            await asyncio.sleep(3)
            event_loop_time = asyncio.get_running_loop().time()
            log.info("current event_loop time %d", event_loop_time)
            new_deadline = event_loop_time + 15
            log.info("reschdule timeout to %d seconds(+15)",new_deadline)
            log.info("suppose 'wakeup_after' wake up at %d", 15 + 3)
            contextManager.reschedule(new_deadline)
            await task

    except asyncio.TimeoutError as err:
        log.info("catch TimeoutError %s",err)

    log.info("task done? %s", task.done())


if __name__ == "__main__":
    start_timestamp = time.perf_counter()
    log.info(f"start {__name__} ...")

    asyncio.run(main(), debug=True)

    log.info(f"{__file__} executed.")
