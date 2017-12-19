import time
import os

import pymongo


def get_conf(conf_file):
    if not os.path.isfile(conf_file):
        print('%s not a file' % conf_file)
        return None

    conf = {}

    with open(conf_file) as _file:
        for line in _file:
            line_data = line.split('=', maxsplit=1)
            if len(line_data) != 2:
                print('%s is invalid', line)
                return None
            conf[line_data[0].strip()] = line_data[1].strip()

    return conf


def get_db(conf):
    return pymongo.MongoClient(conf['url'])[conf['db']]


def write_to_file(filename, items):
    with open(filename, 'a') as _file:
        _file.writelines('%s\n' % '\n'.join(items))


def retry_run(_callable, *args, _wait_minutes=30):
    """ Run the _callable which is some db operation.

    On connection problems, the db operation is retried,
    waiting in incremental intervals until _wait_minutes have elapsed.
    """

    max_pow = 10
    base = 1.37
    # base and max_pow: if one is changed, must change the other so:
    # pow(base, 0) + pow(base, 1) + ..pow(base, max_pow - 1) = 60 (seconds)
    for i in range(max_pow):
        try:
            return _callable(*args)
        except pymongo.errors.ConnectionFailure as err:
            print(err)
            wait_seconds = pow(base, i) * _wait_minutes
            print('Retrying after %.2f seconds (attempt %s/%s)' %
                  (wait_seconds, i + 1, max_pow))
            time.sleep(wait_seconds)

    raise TimeoutError()


def format_time(seconds):
    minute = 60
    hour = minute * 60
    if seconds < minute:
        return '{} sec.'.format(int(seconds))

    if seconds < hour:
        _m = int(seconds / minute)
        _s = int(seconds % minute)
        return '{} min. {} sec.'.format(_m, _s)

    _h = int(seconds / hour)
    seconds = seconds % hour
    _m = int(seconds / minute)
    _s = int(seconds % minute)

    return '{} h. {} min. {} sec.'.format(_h, _m, _s)


def remove_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print('%s was removed' % filename)


def append_to_file(filename, msg):
    with open(filename, 'a') as f_out:
        f_out.write('%s\n' % msg)
