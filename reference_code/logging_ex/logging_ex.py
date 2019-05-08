import logging
import logging.handlers
import time

from orc import Orc

LOG_FMT = '%(asctime)s UTC [%(levelname)s] - %(message)s'
LOG_DATE_FMT = '%Y-%m-%d %H:%M:%S'


def logging_test_1():
    log = logging.getLogger('haha')
    log.setLevel(logging.DEBUG)

    h1 = logging.StreamHandler()
    h1.setLevel(logging.DEBUG)
    h2 = logging.FileHandler('warnings-errors.log')
    h2.setLevel(logging.WARNING)
    formatter = logging.Formatter(
        fmt=LOG_FMT,
        datefmt=LOG_DATE_FMT)
    formatter.converter = time.gmtime
    h1.setFormatter(formatter)
    h2.setFormatter(formatter)

    log.addHandler(h1)
    log.addHandler(h2)

    log.debug('DEBUG BANANA')
    log.info('INFO BANANA')
    log.warning('WARNING BANANA')

    Orc()

# file rotation
def logging_test_2():
    log = logging.getLogger('banana')
    log.setLevel(logging.DEBUG)
    h = logging.handlers.RotatingFileHandler(
        filename='rotating-banana-logger.log',
        maxBytes=200,
        backupCount=2)
    formatter = logging.Formatter(fmt=LOG_FMT,
                          datefmt=LOG_DATE_FMT)
    formatter.converter = time.gmtime
    h.setFormatter(formatter)
    log.addHandler(h)

    for i in range(20):
        log.debug('i = %s' % i)


if __name__ == '__main__':
    logging_test_2()
