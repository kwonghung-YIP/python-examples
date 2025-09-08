import asyncio
import time
import yaml
from pathlib import Path

import logging
from logging.config import dictConfig

class MyFilter(logging.Filter):

    @classmethod
    def factory(cls):
        return MyFilter()
    
    def __init__(self):
        self.__start_timestamp:float = time.perf_counter()

    def filter(self, record:logging.LogRecord) -> bool:
        record.elapse = time.perf_counter() - self.__start_timestamp
        return True

config = {
    "version": 1,
    "formatters": {
        "asyncio_task": {
            "format": "%(asctime)s [%(levelname)s]|%(threadName)s|%(taskName)s|%(elapse)6.3f|%(funcName)s : %(message)s"
        }
    },
    "filters": {
        "myFilter": {
            "()": "main.MyFilter.factory"
        }
    },
    "handlers": {
        "asyncio_console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "asyncio_task",
            "filters": ["myFilter"]
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

cfg = yaml.load_all(Path("logging-config.yaml").read_text())

dictConfig(config)
log = logging.getLogger("asyncio_log")

async def func():
    log.info("hello!")

if __name__  == "__main__":
    asyncio.run(func())