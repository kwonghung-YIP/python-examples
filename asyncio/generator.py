import asyncio
import logging

logging.basicConfig(level=logging.INFO)

log = logging.getLogger(__name__)

class _49Exception(Exception):
    """49 Exception"""

def generator_func():
    try:
        for i in range(1,101):
            result = (yield i)
            log.info(f"caller told me that {i} is {result}")
    except _49Exception:
        log.info("expect _49Exception")
    finally:
        log.info("generator completed")

async def async_generator_func():
    try:
        for i in range(1,101):
            await asyncio.sleep(1)
            result = (yield i)
            log.info(f"caller told me that {i} is {result}")
    except _49Exception:
        log.info("expect _49Exception")
    finally:
        log.info("generator completed")    

def run_generator() -> None:
    generator = generator_func()
    log.info(type(generator)) # type of g is 'generator'
    try:
        i = next(generator)
        while True:
            log.info(i)
            if i == 49:
                generator.throw(_49Exception())
            elif i <= 50:
                i = generator.send("even" if i%2==0 else "odd")
            else:
                log.info("close generator...")
                generator.close()
                break
    except StopIteration:
        log.info("end of generator")

async def run_async_for() -> None:
    async for i in async_generator_func():
        log.info(i) 

async def run_async_generator() -> None:
    async_generator = async_generator_func()
    log.info(type(async_generator))
    try:
        i = await anext(async_generator)
        while True:
            log.info(i)
            if i == 49:
                await async_generator.athrow(_49Exception())
            elif i <= 50:
                i = await async_generator.asend("even" if i%2==0 else "odd")
            else:
                log.info("close generator...")
                await async_generator.aclose()
                break
    except StopAsyncIteration:
        log.info("end of async_generator")

if __name__ == "__main__":
    run_generator()
    asyncio.run(run_async_for())
    asyncio.run(run_async_generator())

    