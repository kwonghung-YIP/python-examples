import logging
import time

class MyFilter(logging.Filter):

    @classmethod
    def factory(cls):
        return MyFilter()
    
    def __init__(self):
        self.__start_timestamp:float = time.perf_counter()

    def filter(self, record:logging.LogRecord) -> bool:
        record.elapse = time.perf_counter() - self.__start_timestamp
        return True