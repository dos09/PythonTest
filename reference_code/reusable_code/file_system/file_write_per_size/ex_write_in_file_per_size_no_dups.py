from datetime import datetime, timezone
import os
import json

import pymongo

class Filter:

    def __init__(self, unique_field):
        """ Parameters:
        - unique_field - this field will be used to uniquely identify 
        mongo document
        """
        self.field_name = unique_field
        self.processed_values = set()

    def is_processed(self, doc):
        value = doc[self.field_name]
        if value is None:
            print('%s is None for document _id = %s' % 
                  (self.field_name, doc['_id']))
            return True # don't process that document

        _is_processed = value in self.processed_values
        if not _is_processed:
            self.processed_values.add(value)

        return _is_processed


class FileWriter:
    MAX_BYTES_PER_FILE = 100
    SINGLE_WRITE_MAX_BYTES = 10

    def __init__(self, dirname, filter_obj=None):
        """ Write mongo documents in JSON file(s).
        Each file's max size is not much bigger than MAX_BYTES_PER_FILE.
        The name of each file is <utc timestamp>.json
        Parameters:
        - dirname: where to write the JSON files
        - filter_obj: against writing duplicate documents. Duplication is
        recognized based on one of the document's fields
        """
        
        self.fname = None
        # amount of bytes in self.fname after current/next write operation
        self.total_bytes = 0
        self.dirname = dirname
        self.filter_obj = filter_obj

    def _get_new_fname(self):
        # without timezone.utc, timestamp assumes local time
        _fname = ('%s.json' %
                  datetime.utcnow().replace(tzinfo=timezone.utc).timestamp())
        _fname = os.path.join(self.dirname, _fname)
        print('new file to write in:', _fname)
        return _fname

    def write_data(self, docs):
        lines = []
        curr_bytes = 0
        for doc in docs:
            if not self.filter_obj or not self.filter_obj.is_processed(doc):
                # TODO use my json_serializer method
                line = '%s\n' % json.dumps(doc, default=str)
                lines.append(line)
                line_len = len(line)
                self.total_bytes += line_len
                curr_bytes += line_len
                
            if curr_bytes >= self.SINGLE_WRITE_MAX_BYTES:
                print('Writing batch of %s bytes (total %s)' %
                      (curr_bytes, self.total_bytes))
                self._write(lines)
                curr_bytes = 0
                lines = []

        if curr_bytes:
            print('Writing batch of %s bytes (total %s)' %
                  (curr_bytes, self.total_bytes))
            self._write(lines)

    def _write(self, lines):
        if self.fname is None:
            self.fname = self._get_new_fname()

        with open(self.fname, 'a') as f_out:
            f_out.writelines(''.join(lines))

        if self.total_bytes >= self.MAX_BYTES_PER_FILE:
            self.fname = None
            self.total_bytes = 0
            print('reset total bytes')


def run():
    db = pymongo.MongoClient()['mytest']
    docs = list(db.orcs.find({}))
    if not docs:
        print('No documents found')
        return

    dirname = r'output'
    filter_obj = Filter('clan')
    fw = FileWriter(dirname, filter_obj)
    fw.write_data(docs)

if __name__ == '__main__':
    print('Started')
    run()
    print('Finished')
