import os


class Humanoid:
    TYPE = 'Humanoid'

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '%s: %s' % (self.TYPE, self.name)


def abs_fname(fname_caller, fname):
    return os.path.join(os.path.dirname(fname_caller), fname)


def print_file(fname):
    #print('Using %s' % os.path.abspath(fname))
    with open(fname, 'r') as fin:
        print(fin.read())
