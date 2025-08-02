import time
import logging
import asyncio

start_timestamp: float

def add_elapse_time(record:logging.LogRecord) -> bool:
    record.elapse = time.perf_counter() - start_timestamp
    return True

LOG_FORMAT = '%(asctime)s [%(levelname)s] : %(message)s'
TASK_LOG_FORMAT = '%(asctime)s [%(levelname)s]|%(threadName)s|%(taskName)s|%(elapse)6.3f : %(message)s'
logging.basicConfig(format=LOG_FORMAT,level=logging.DEBUG)

formatter = logging.Formatter(fmt=TASK_LOG_FORMAT)

handler = logging.StreamHandler()
handler.setFormatter(formatter)
handler.addFilter(add_elapse_time)

log = logging.getLogger(__name__)
log.propagate = False
log.addHandler(handler)

async def long_running():
    log.info("long_running: started...")

    try:
        while True:
            log.info("long_running: time.sleep for 2 seconds...")
            time.sleep(2)
            log.info("long_running: asyncio.sleep for 30 seconds...")
            await asyncio.sleep(30)
            log.info("long_running: wake up after %d seconds", 30)
    except asyncio.CancelledError as err:
        log.info("long_running: catch CancelledError %s", err)
        #raise err
    finally:
        log.info("long_running_func: completed")

async def report_status(target:asyncio.Task):
    while not target.done():
        await asyncio.sleep(1)
        log.info("task[%s] report status: cancelled[%s], done[%s]", target.get_name(), target.cancelled(), target.done())    

async def cancel_task(target:asyncio.Task):
    log.info("start cancel task...")
    while not target.done():
        await asyncio.sleep(10)
        successCancel = target.cancel("cancel() request from canel_task")
        log.info("cancel task[%s] success? %s, cancelled? %s cancelling? %d", target.get_name(), successCancel, target.cancelled(), target.cancelling())
    
async def main():
    t1 = asyncio.create_task(long_running(),name="t1")
    t2 = asyncio.create_task(report_status(t1),name="t2")
    t3 = asyncio.create_task(cancel_task(t1),name="t3")

    await asyncio.gather(t1,t2,t3)

if __name__ == "__main__":
    start_timestamp = time.perf_counter()
    log.info(f"start {__name__} ...")

    asyncio.run(main())

    log.info(f"{__file__} executed.")
