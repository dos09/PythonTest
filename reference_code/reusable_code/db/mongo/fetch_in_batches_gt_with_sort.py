import logging
import time
from datetime import datetime
from bson import json_util
from collections import OrderedDict

import pymongo


LOG = logging.getLogger(__name__)
ch = logging.StreamHandler()
ch.setFormatter(logging.Formatter(
    "[%(asctime)s] [%(levelname)8s] "
    "--- %(message)s (%(filename)s:%(lineno)s)", "%Y-%m-%d %H:%M:%S"))
LOG.addHandler(ch)
LOG.setLevel('DEBUG')


def get_mongo_db_con(url, db_name):
    return getattr(pymongo.MongoClient(url), db_name)


def retry_run(_callable, *args, **kwargs):
    for i in range(10):
        try:
            return _callable(*args, **kwargs)
        except pymongo.errors.ConnectionFailure as err:
            LOG.warning(err)
            timeout = i * 60 / 2 + 1
            LOG.info('Retrying in %s seconds (%d)', timeout, i + 1)
            time.sleep(timeout)

    raise TimeoutError()


def batch_fetch_using_sort(db, collection_name, find_query=None,
                           fetch_fields=None, sort_by_field='_id',
                           batch_limit=10000, matching_docs_count=None):
    """ Fetch data in batches.

    Instead of skip/limit batch fetching which is slow for large volumes
    of data, use the following approach:
    1. Filter by <find_query>, sort in ascending order by 
    <sort_by_field> and take one batch of documents.
    2. Now add to <find_query> the condition <sort_by_field> to be > X, 
    where X is the value taken from the <sort_by_field> of the most 
    recently fetched document (last document of each batch).
    3. Repeat step 2 while data is available 

    !!! ATTENTION !!!
        <sort_by_field> must be unique ($gt is used), and MUST
        exist in all documents

    Yield a batch of documents
    """
    def query(limit_size):
        return list(collection.find(find_query, fetch_fields)
                    .sort(sort_by).limit(limit_size))

    if find_query is None:
        find_query = {}
    if fetch_fields is None:
        fetch_fields = {}

    collection = db[collection_name]
    find_query = dict(find_query)
    fetch_fields = dict(fetch_fields)
    fetch_fields[sort_by_field] = 1
    sort_by = [(sort_by_field, pymongo.ASCENDING)]
    if matching_docs_count is None:
        LOG.info('Counting documents for processing from %s', collection_name)
        matching_docs_count = retry_run(collection.count, find_query)
    LOG.info('Documents from %s for processing: %s',
             collection_name, matching_docs_count)
    if not matching_docs_count:
        return
    processed_docs_count = 1
    progress_text = (r'Processed {0:>%d}/%d documents from %s [{1:6.2f}%%]' %
                     (len(str(matching_docs_count)), matching_docs_count,
                      collection_name))
    while True:
        docs = retry_run(query, batch_limit)
        if not docs:
            break
        yield docs

        find_query[sort_by_field] = {'$gt': docs[-1][sort_by_field]}
        processed_docs_count += len(docs)
        percent = (processed_docs_count / matching_docs_count) * 100
        LOG.info(progress_text.format(processed_docs_count, percent))


if __name__ == '__main__':
    mongo_url = 'mongodb://localhost:27017'
    mongo_db_name = 'rimm'
    db = get_mongo_db_con(mongo_url, mongo_db_name)
    for docs in batch_fetch_using_sort(
            db=db, collection_name='vulnerabilitiesGrid',
            _find_query={'related.threatModelSims': '3uzC6dv9AKE6M5m4L'},
            _fetch_fields={'info.name': 1}):
        print(docs)
