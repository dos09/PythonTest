import pymongo
db = pymongo.MongoClient()['mytest']
# print(db.command('ping').get('ok'))


def retry_run(_callable, *args, _wait_minutes=30):
    print('wait minutes =', _wait_minutes)
    max_pow = 10
    base = 1.37
    # base and max_pow: if one is changed, must change the other so:
    # pow(base, 0) + pow(base, 1) +... pow(base, max_pow - 1) = 1 min
    for i in range(max_pow):
        try:
            return _callable(*args)
        except pymongo.errors.ConnectionFailure as err:
            wait_time = pow(base, i) * _wait_minutes
            print('wait for %.2f secs' % wait_time)
            print(err)
            print('Retrying %s/%s' % (i + 1, max_pow))

    raise TimeoutError()

res = retry_run(db.orcs.find_one,
                {'clan': 'Black wolfs'},
                ['clan', 'name'],
                _wait_minutes=2)
print(res)
