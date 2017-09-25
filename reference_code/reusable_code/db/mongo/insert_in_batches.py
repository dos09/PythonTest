import pymongo


class Example:

    def __init__(self):
        self.db = pymongo.MongoClient()['mytest']

    def insert_in_batches(self, collection_name, docs, batch_size=1000):
        if not docs:
            return
        
        all_count = len(docs)
        curr_count = 0
        progress_text = '* Inserted {0:>%d}/%d [{1:6.2f} %%]' % (
            len(str(all_count)), all_count)
        bulk = self.db[collection_name].initialize_unordered_bulk_op()
        for doc in docs:
            bulk.insert(doc)
            curr_count += 1
            if curr_count % batch_size == 0 or curr_count == all_count:
                bulk.execute()
                bulk = self.db[collection_name].initialize_unordered_bulk_op()
                percent = curr_count * 100. / all_count
                print(progress_text.format(curr_count, percent))

    def test(self):
        data = [
            {'str': 'edno', 'num': 1},
            {'str': 'dve', 'num': 2},
            {'str': 'tri', 'num': 3}
        ]
        self.insert_in_batches('tralala', data, batch_size=2)

Example().test()