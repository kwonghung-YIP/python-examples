import time
import logging
import asyncio

LOG_FORMAT = '%(asctime)s [%(levelname)s] %(message)s'
logging.basicConfig(format=LOG_FORMAT,level=logging.DEBUG)

log = logging.getLogger(__name__)

start_timestamp: float

def tasklog(msg:str, *args):
    task = asyncio.current_task()
    elapsed = time.perf_counter() - start_timestamp
    log.log(logging.INFO,"task[%s] after %d sec:",task.get_name(),elapsed)

async def long_running():
    tasklog("Hello")
    task = asyncio.current_task()
    tname = task.get_name()

    s = time.perf_counter()
    log.info("long_running_func[%s]: started...",tname)

    cancelCnt = 0
    while cancelCnt <= 3:
        try:
            elapsed = time.perf_counter() - s
            log.info("long_running_func[%s]: elapsed: %d, time.sleep for 2 seconds...", tname, elapsed)
            time.sleep(2)
            elapsed = time.perf_counter() - s
            log.info("long_running_func[%s]: elapsed: %d, asyncio.sleep for 30 seconds...", tname, elapsed)
            await asyncio.sleep(30)
            elapsed = time.perf_counter() - s
            log.info("long_running_func[%s]: wake up after %d seconds", tname, elapsed)
        except asyncio.CancelledError as err:
            elapsed = time.perf_counter() - s
            log.info("long_running_func[%s]: catch CancelledError %s after %d seconds", tname, err, elapsed)
            raise err

    elapsed = time.perf_counter() - s
    log.info("long_running_func[%s]: completed",tname)

async def report_status(target:asyncio.Task):
    s = time.perf_counter()
    while not target.done():
        await asyncio.sleep(1)
        elapsed = time.perf_counter() - s
        log.info("task[%s] report status after %d seconds: cancelled[%s], done[%s]", target.get_name(), elapsed, target.cancelled(), target.done())    

async def cancel_task(target:asyncio.Task):
    s = time.perf_counter()
    log.info("start cancel task...")
    while not target.done():
        await asyncio.sleep(10)
        elapsed = time.perf_counter() - s
        successCancel = target.cancel("cancel() request from canel_task")
        log.info("cancel task[%s] after %d seconds success? %s, cancelled? %s cancelling? %d", target.get_name(), elapsed, successCancel, target.cancelled(), target.cancelling())
    
async def main():
    t1 = asyncio.create_task(long_running(),name="t1")
    t2 = asyncio.create_task(report_status(t1),name="t2")
    t3 = asyncio.create_task(cancel_task(t1),name="t3")

    await asyncio.gather(t1,t2,t3)

if __name__ == "__main__":
    start_timestamp = time.perf_counter()
    log.info(f"start {__name__} ...")

    asyncio.run(main())

    elapsed = time.perf_counter() - start_timestamp
    log.info(f"{__file__} executed in {elapsed} seconds.")
