import os

from dateutil.parser import parse


def run():
    print('p1 -> p.py')
    fname = os.path.join(os.path.dirname(__file__), 'p.txt')
    with open(fname) as fin:
        print(fin.read())

    d = parse('2018-01-19')
    print(d, type(d))


if __name__ == '__main__':
    run()
