import pymongo
import time

import common

FILE_NAME = 'skip_limit_data'


def _run():
    """ Write all _id-s from ip collection to file,
    record in another file the elapsed time.
    To fetch the data skip/limit is used
    """
    
    conf = common.get_conf('conf')
    if not conf:
        return

    db = common.get_db(conf)
    db_collection = db.ip
    criteria = {}
    fetch_fields = {
        '_id': 1
    }
    offset = 0
    batch_limit = 1000  # TODO try with 3000
    all_docs_count = db_collection.count(criteria)
    processed_docs_count = 0
    write_limit = 50000
    ids_to_write = []
    while True:
        docs = list(common.retry_run(
            db_collection.find(criteria, fetch_fields).skip(offset).limit,
            batch_limit))
        
        if not docs:
            break

        offset += batch_limit
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
    print(' > Testing skip limit pagination')
    common.remove_file(FILE_NAME)
    start_time = time.time()
    _run()
    seconds_elapsed = time.time() - start_time
    time_msg = ('Time elapsed %s (skip limit)' % 
                common.format_time(seconds_elapsed))
    print(time_msg)
    common.append_to_file('times', time_msg)
    print('Data is in %s' % FILE_NAME)
    return FILE_NAME

if __name__ == '__main__':
    run()
