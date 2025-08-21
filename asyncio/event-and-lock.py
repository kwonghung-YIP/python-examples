import asyncio
import contextvars
import logging

logging.basicConfig(level=logging.INFO)

log = logging.getLogger("asyncLogger")

counter = contextvars.ContextVar("counter",default=0)
context = contextvars.copy_context()

async def counting(event:asyncio.Event,lock:asyncio.Lock):
    try:
        log.info("waiting for the event being set...")
        await event.wait()
        log.info("waiting for acquiring the lock...")
        async with lock:
            i = 1
            while i <= 5:
                await asyncio.sleep(1)
                cnt = counter.get()
                cnt += 1
                log.info(f"increasing counter by 1:{cnt}")
                counter.set(cnt)
                i += 1
            log.info("finish and release lock.")
    except asyncio.CancelledError as err:
        log.info("catch CancelledError")
        raise err

async def toggleEvent(event:asyncio.Event,sleep):
    await asyncio.sleep(sleep)
    log.info(f"set event after {sleep} sec")
    event.set()

async def main():
    event = asyncio.Event()
    lock = asyncio.Lock()

    awaitables = [ asyncio.create_task(counting(event,lock),context=context)
        for _ in range(1,11) ]
    awaitables.append(toggleEvent(event,5))

    await asyncio.gather(*awaitables)
    log.info(f"main() completed")


if __name__ == "__main__":
    asyncio.run(main())
    log.info(f"{__name__} completed")