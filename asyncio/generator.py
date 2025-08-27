import logging

logging.basicConfig(level=logging.INFO)

log = logging.getLogger(__name__)

class _49Exception(Exception):
    """49 Exception"""

def generator():
    try:
        for i in range(1,101):
            result = (yield i)
            log.info(f"caller told me that {i} is {result}")
    except _49Exception:
        log.info("expect _49Exception")
    finally:
        log.info("generator completed")

if __name__ == "__main__":
    g = generator()
    log.info(type(g)) # type of g is 'generator'
    try:
        i = next(g)
        while True:
            log.info(i)
            if i == 49:
                g.throw(_49Exception())
            elif i <= 50:
                i = g.send("even" if i%2==0 else "odd")
            else:
                log.info("close generator...")
                g.close()
                break
    except StopIteration:
        log.info("end of generator")

    
    