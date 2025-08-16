import asyncio
import contextvars
import time
import random
import logging

queueStatus = contextvars.ContextVar('queueStatus',default="active")
sharedContext = contextvars.copy_context()

logging.basicConfig(level=logging.INFO)

log = logging.getLogger("asyncLogger")

class StopThreadGroupException(Exception):
    """Customized exception to stop ThreadGroup"""

async def consumer(queue:asyncio.Queue):
    while True:
        try:
            log.info("waiting for new message from the queue...")
            msg = await queue.get()
            log.info(f"message received [{msg}]")
            queue.task_done()
        except asyncio.CancelledError as err:
            log.info("the task was cancelled")
            break

async def producer(queue:asyncio.Queue,noOfMsg:int):
    i:int = 0
    while i <= noOfMsg:
        try:
            msg = f"msg-{i}"
            log.info(f"sending msg {msg} to queue...")
            await queue.put(msg)
            interval = random.randint(1,10)
            log.info(f"sleep for {interval} sec...")
            await asyncio.sleep(interval)
            i += 1
        except asyncio.CancelledError as err:
            log.info("the task was cancelled")
            raise err

async def producerGroup(queue:asyncio.Queue):
    try:
        log.info("start producer thread group...")
        async with asyncio.TaskGroup() as tg:
            producers = [tg.create_task(producer(queue,10), \
                   name=f"producer-{x}") for x in range(5)]
            tg.create_task(stopThreadGroup(),context=sharedContext)
    except* StopThreadGroupException:
        log.info("producer thread group completed.")
    except* asyncio.CancelledError:
        log.info("ptg catch CancelledError.")

async def consumerGroup(queue:asyncio.Queue):
    try:
        log.info("start consumer thread group...")
        async with asyncio.TaskGroup() as tg:
            consumers = [tg.create_task(consumer(queue), \
                   name=f"producer-{x}") for x in range(5)]
            tg.create_task(stopThreadGroup(),context=sharedContext)
    except* StopThreadGroupException:
        log.info("consumer thread group completed.")
    except* asyncio.CancelledError:
        log.info("ctg catch CancelledError.")

async def monitor(queue:asyncio.Queue):
    while True:
        try:
            log.info(f"queue size: {queue.qsize()} full? {queue.full()}")
            if (queue.full()):
                await asyncio.sleep(10)
                log.info("update queue status to 'full'")
                queueStatus.set("full")
                break
            else:
                await asyncio.sleep(1)
        except asyncio.CancelledError as err:
            log.info(f"catch cancelledError, update queue status to shutdown")
            queueStatus.set("shutdown")
            raise err

async def stopThreadGroup():
    while True:
        status = queueStatus.get()
        log.info(f"queue status:{status}")
        if status == "active":
            await asyncio.sleep(1)
        else:
            log.info("raise StopThreadGroupException")
            raise StopThreadGroupException()

async def main():
    try:
        queue = asyncio.Queue(10)
        async with asyncio.timeout(60*5):
            monTask = asyncio.create_task(monitor(queue), \
                        name="monitor",context=sharedContext)
            pgTask = asyncio.create_task(producerGroup(queue))
            cgTask = asyncio.create_task(consumerGroup(queue))
            await asyncio.gather(monTask,pgTask,cgTask)
    except TimeoutError as err:
        log.info("main thread timeout")    


if __name__ == "__main__":
    asyncio.run(main())