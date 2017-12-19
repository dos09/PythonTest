from datetime import datetime, timezone
import os
import json

import pymongo


class FileWriter:
    MAX_BYTES_PER_FILE = 100
    SINGLE_WRITE_MAX_BYTES = 10

    def __init__(self, dirname):
        self.fname = None
        # amount of bytes in self.fname after current/next write operation
        self.total_bytes = 0
        self.dirname = dirname

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
    fw = FileWriter(dirname)
    fw.write_data(docs)

if __name__ == '__main__':
    print('Started')
    run()
    print('Finished')
