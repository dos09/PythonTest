import pymongo
import time
from datetime import datetime

import common

FILE_NAME = 'find_limit_data_isActive_ts_h'


def _run():
    """ Write all _id-s from ip collection to file,
    record in another file the elapsed time.
    To fetch the data find/limit is used (using the _id of the last
    processed document as filter)
    
    !!! THIS APPROACH IS APPLICABLE ONLY IF THE _id IS OF TYPE ObjectId
    """

    conf = common.get_conf('conf')
    if not conf:
        return

    db = common.get_db(conf)
    db_collection = db.ip
    criteria = {
        'isActive.ts.h': {'$gt': datetime(1991, 1, 1)}
    }
    fetch_fields = {
        '_id': 1,
        'isActive.ts.h':1
    }
    batch_limit = 1000  # TODO try with 3000
    all_docs_count = db_collection.count(criteria)
    write_limit = 50000
    ids_to_write = []
    sort_field = [('isActive.ts.h', pymongo.ASCENDING)]
    docs = list(db_collection.find(criteria).sort(sort_field).limit(1))
    if not docs:
        print('Collection %s is empty' % db_collection)
        return
    
    last_h = docs[0]['isActive']['ts']['h']
    ids_to_write.append(str(docs[0]['_id']))
    processed_docs_count = 1
    while True:
        criteria = {
            'isActive.ts.h': {'$gt': last_h}
        }
        docs = list(common.retry_run(db_collection.find(criteria, fetch_fields)
                                     .sort(sort_field).limit, batch_limit))
        if not docs:
            break

        last_h = docs[-1]['isActive']['ts']['h']
        ids_to_write.extend([str(doc['_id']) for doc in docs])
        if len(ids_to_write) > write_limit:
            common.write_to_file(FILE_NAME, ids_to_write)
            ids_to_write = []

        processed_docs_count += len(docs)
        percent = (processed_docs_count * 100.) / all_docs_count
        print(' * Processed %d/%d [%6.2f]' %
              (processed_docs_count, all_docs_count, percent))

    if ids_to_write:
        common.write_to_file(FILE_NAME, ids_to_write)


def run():
    print(" > Testing pagination using the last document's isActive.ts.h (find/limit)")
    common.remove_file(FILE_NAME)
    start_time = time.time()
    _run()
    seconds_elapsed = time.time() - start_time
    time_msg = ('Time elapsed %s (find limit isActive)' %
                common.format_time(seconds_elapsed))
    print(time_msg)
    common.append_to_file('times', time_msg)
    print('Data is in %s' % FILE_NAME)
    return FILE_NAME

if __name__ == '__main__':
    run()
