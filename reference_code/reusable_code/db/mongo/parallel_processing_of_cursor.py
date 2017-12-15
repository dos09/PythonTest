import multiprocessing
import os

import pymongo

# process in parallel cursor results

USE_LOCAL_DB = True
PREF_PROCS_COUNT = 4

M3_URL = 'X'
M3_DB = 'X'

LOCAL_URL = 'mongodb://127.0.0.1:27017'
LOCAL_DB = 'org_backup'


def get_db(mongo_url, mongo_db_name):
    return pymongo.MongoClient(mongo_url)[mongo_db_name]


def get_borders(all_docs_count, procs_count):
    if all_docs_count <= procs_count:
        print('count of worker processes set to 1')
        procs_count = 1

    if procs_count == 1:
        return [(0, all_docs_count)]  # one range for all

    step = all_docs_count // procs_count
    low = 0
    borders = []  # low - inclusive, high - exclusive
    for i in range(procs_count - 1):
        high = low + step
        borders.append((low, high))
        low = high

    borders.append((low, all_docs_count))

    return borders


def get_batch_limit(l, h, pref_limit):
    items_count = h - l
    if items_count < pref_limit:
        pref_limit = items_count

    return pref_limit


def run_ip_worker(mongo_url, mongo_db_name, criteria, low, high):
    db = get_db(mongo_url, mongo_db_name)
    pref_limit = 2  # TODO:
    offset = low
    while offset < high:
        curr_limit = get_batch_limit(offset, high, pref_limit)
        docs = list(db.ip.find(criteria).skip(offset).limit(curr_limit))
        if not docs:
            break

        offset += curr_limit

        for doc in docs:
            print('%s %s' % (os.getpid(), doc['_id']))


def run(mongo_url, mongo_db_name):
    db = get_db(mongo_url, mongo_db_name)
    org_ids = [309]
    criteria = {'r_orgs': {'$in': org_ids}}
    all_docs_count = db.ip.count(criteria)
    print('Found %s IP-s' % all_docs_count)
    borders = get_borders(all_docs_count, PREF_PROCS_COUNT)
#     for l, h in borders:
#         print(l, h)
    procs = []
    for l, h in borders:
        kwargs = {
            'mongo_url': mongo_url,
            'mongo_db_name': mongo_db_name,
            'criteria': criteria,
            'low': l,
            'high': h
        }
        p = multiprocessing.Process(target=run_ip_worker, kwargs=kwargs)
        procs.append(p)
        p.start()

    for p in procs:
        p.join()

    print('Finished execution')

if __name__ == '__main__':
    if USE_LOCAL_DB:
        mongo_url = LOCAL_URL
        mongo_db_name = LOCAL_DB
    else:
        mongo_url = M3_URL
        mongo_db_name = M3_DB

    multiprocessing.set_start_method('spawn')
    run(mongo_url, mongo_db_name)
