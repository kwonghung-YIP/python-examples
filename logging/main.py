import asyncio
import logging
from logging.config import dictConfig

config = {
    "version": 1,
    "formatters": {
        "asyncio_task": {
            "format": "%(asctime)s [%(levelname)s]|%(threadName)s|%(taskName)s|%(funcName)s : %(message)s"
        }
    },
    "filters": {
        "filter1": {
            "name": "asyncio_log"
        }
    },
    "handlers": {
        "asyncio_console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "asyncio_task",
            "filters": ["filter1"]
        }
    },
    "loggers": {
        "asyncio_log": {
            "level": "INFO",
            "propagate": "false",
            "handlers": ["asyncio_console"]
        }
    }
}

dictConfig(config)
log = logging.getLogger("asyncio_log")

async def func():
    log.info("hello!")

if __name__  == "__main__":
    asyncio.run(func())