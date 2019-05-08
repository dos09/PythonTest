import logging

LOG = logging.getLogger('haha')


class Orc:

    def __init__(self):
        LOG.debug('DEBUG ORC')
        LOG.info('INFO ORC')
        LOG.warning('WARNING ORC')
        LOG.error('ERROR ORC')
