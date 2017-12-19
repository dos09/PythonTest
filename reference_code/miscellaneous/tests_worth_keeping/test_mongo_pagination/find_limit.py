import pymongo
import time

import common

FILE_NAME = 'find_limit_data'


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
    criteria = {}
    fetch_fields = {
        '_id': 1
    }
    batch_limit = 1000  # TODO try with 3000
    all_docs_count = db_collection.count(criteria)
    write_limit = 50000
    ids_to_write = []
    docs = list(db_collection.find(criteria).limit(1))
    if not docs:
        print('Collection %s is empty' % db_collection)
        return
    
    last_id = docs[0]['_id']
    ids_to_write.append(str(last_id))
    processed_docs_count = 1
    while True:
        criteria = {'_id': {'$gt': last_id}}
        docs = list(common.retry_run(db_collection.find(criteria, fetch_fields)
                                     .limit, batch_limit))
        if not docs:
            break

        last_id = docs[-1]['_id']
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
    print(" > Testing pagination using the last document's _id (find/limit)")
    common.remove_file(FILE_NAME)
    start_time = time.time()
    _run()
    seconds_elapsed = time.time() - start_time
    time_msg = ('Time elapsed %s (find limit)' %
                common.format_time(seconds_elapsed))
    print(time_msg)
    common.append_to_file('times', time_msg)
    print('Data is in %s' % FILE_NAME)
    return FILE_NAME

if __name__ == '__main__':
    run()
