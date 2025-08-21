import asyncio
import logging
import random

logging.basicConfig(level=logging.INFO)

log = logging.getLogger("asyncLogger")

async def sleepAndRun(maxSleep:float):
    task = asyncio.current_task()
    try:
        sleep = round(random.uniform(0,maxSleep),4)
        log.info("sleep for %f seconds...",sleep)
        await asyncio.sleep(sleep)
        log.info("awake after %f seconds!",sleep)
        return f"{task.get_name()} completed after {sleep} secs!"
    except asyncio.CancelledError as err:
        log.info(f"{task.get_name()} catch CancelledError {err}")
        raise err

async def main():
    tasks = [asyncio.create_task(sleepAndRun(30),name=f"task-{i}") for i in range(1,11)]
    done, pending = await asyncio.wait(tasks,
        timeout=20,return_when=asyncio.ALL_COMPLETED)
    
    for t in done:
        log.info(f"{t.get_name()} is done? {t.done()}, result:{t.result()}")
        log.info(t)

    # asyncio.wait will not cancel the pending tasks run over the timeout parameter
    for t in pending:
        log.info(f"{t.get_name()} is done? {t.done()} cancelled? {t.cancelled()}")
        log.info(t)

    # allowing the pending tasks to run 5 more seconds
    # for those pending tasks run over more than 25 seconds,
    # they will receive the CancelledError when stop the event_loop while exiting main()
    await asyncio.sleep(5)
    log.info(f"main() completed")


if __name__ == "__main__":
    asyncio.run(main())
    log.info(f"{__name__} completed")