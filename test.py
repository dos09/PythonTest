import pymongo


def print_in_batches(db):
    limit = 2
    offset = 0
    while True:
        data = list(db.nums.find({}).skip(offset).limit(limit))
        if not data:
            break
        end = offset + limit
        print('Fetched data from %s to %s' % (offset, end))
        print(data)
        offset = end


def modify_in_batches(db):
    limit = 2
    while True:
        # no skipping is needed because we change the found documents
        # so they won't match the search criteria
        docs = list(db.nums.find({'value': {'$gte': 1}}).limit(limit))
        if not docs:
            break

        print(docs)

        for doc in docs:
            doc['value'] = 0
            db.nums.replace_one({'_id': doc['_id']}, doc)

db = pymongo.MongoClient('mongodb://localhost:27017')['mytest']
count = db.nums.find({}).count()
print(count, 'records found in nums collection')

# print_in_batches(db)
modify_in_batches(db)
