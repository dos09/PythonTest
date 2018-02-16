import pymongo


class Example:

    def __init__(self):
        self.db = pymongo.MongoClient()['mytest']

    def fetch_in_batches(self, collection_name, batch_size=5000,
                         criteria={}, fetch_fields=None):
        all_count = self.db[collection_name].find({}).count()
        curr_size = 0
        progress_text = '* Processed {0:>%d}/%d [{1:6.2f} %%]' % (
            len(str(all_count)), all_count)
        offset = 0
        while True:
            data = list(self.db[collection_name].find(
                criteria, fetch_fields).skip(offset).limit(batch_size))
            if not data:
                break

            offset += batch_size
            yield data  # log progress after the data was processed
            curr_size += len(data)
            percent = curr_size * 100. / all_count
            # TODO: for work replace with LOG
            print(progress_text.format(curr_size, percent))

    def test(self):
        for data in self.fetch_in_batches('orcs', batch_size=3):
            print(data)

Example().test()