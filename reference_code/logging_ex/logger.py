import logging

def test1():
    log = logging.getLogger('orcs')
    log.addHandler(logging.StreamHandler())
    log.setLevel('DEBUG')
    log.debug('debug: %s %s %s', 'just', 'an', 'orc')
    log.info('info')
    log.warning('warning')
    log.error('error')
    log.critical('critical')
    
def test2():
    logger = logging.getLogger('simple_example')
    logger.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    # ch.setFormatter(logging.Formatter('%(asctime)s [%(levelname)8s] - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))
    ch.setFormatter(logging.Formatter("[%(asctime)s] [%(levelname)8s] --- %(message)s (%(filename)s:%(lineno)s)", "%Y-%m-%d %H:%M:%S"))
    logger.addHandler(ch)
     
    # 'application' code
    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')
    
test2()