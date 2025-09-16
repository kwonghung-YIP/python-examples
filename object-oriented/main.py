import logging

from domain.common import *

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

if __name__ == "__main__":
    john = Person("John","Doe")
    john.title = Title.MR
    john.email = "abc@yahoo.com"
    log.info(john)
    log.info(type(john))

    del john.title
    john.title = Title.MR

    peter = Person("Peter","Pan")
    peter.title = Title.MR
    peter.email = "peter.pan@gmail.com"

    log.info("%s,%s,%s,%s",john,john.email,peter,peter.email)

    Person.email = "unknown2"

    log.info("%s,%s,%s,%s",john,john.email,peter,peter.email)
