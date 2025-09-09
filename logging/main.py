import asyncio
import logging
import packageA

log = logging.getLogger("asyncio_log")

async def func():
    log.info("hello!")

if __name__  == "__main__":
    asyncio.run(func())