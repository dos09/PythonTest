# https://docs.python.org/3/library/itertools.html
import itertools


def print_method_name(func):

    def wrapper(*args, **kwargs):
        s = 'running method "%s"' % func.__name__
        dashes = len(s) * '-'
        print('{0}\n{1}\n{0}'.format(dashes, s))
        return func(*args, **kwargs)

    return wrapper


@print_method_name
def infinite_interators():
    """
    count, cycle, repeat
    
    itertools.count(start=1, step=10):
        1, 10, 20, 30, 40 ... forever
    itertools.cycle([1,2,3]):
        1, 2, 3, 1, 2, 3, 1, 2, 3 ... forever
    itertools.repeat(100)
        100, 100, 100, 100 ... forever
        
    Using map to demonstrate the usage of the above methods
    map(function, iterable [, iterable]*)
        map will iterate until the shortest iterable is exhausted
    """

    def mofo(*args):
        return 'args = %s, sum = %s' % (args, sum(args))

    r = map(
        mofo,
        [0, 1, 2, 3, 4, 5],
        itertools.count(start=0, step=10),
        itertools.cycle([1, 2, 3]),
        itertools.repeat(100))
    for e in r:
        print(e)

"""
Iterators terminating on the shortest input sequence
(not all only what seems to be more useful)
"""


@print_method_name
def m_accumulate():

    def mofo(a, b):
        print(a, b)
        return b * 10

    arr = [1, 2, 3, 4]
    res = list(itertools.accumulate(arr))
    print('input', arr)
    print('output', res)

    res = list(itertools.accumulate(arr, mofo))
    print('input', arr)
    print('output', res)


@print_method_name
def m_chain():
    a = [1, 2, 3, 4]
    b = [10, 20, 30]
    r = list(itertools.chain(a, b))
    print(r)


@print_method_name
def m_compress():
    arr = ['a', 'b', 'e', 'o', 'r', 'f']
    selectors = [1, 0, 1, 1, 0, 0]
    r = list(itertools.compress(arr, selectors))
    print(r)


@print_method_name
def m_filterfalse():
    iterable = [0, 1, 2, True, False, '', 'banana']
    predicate = bool
    r = list(itertools.filterfalse(predicate, iterable))
    print(r)

@print_method_name
def m_zip_longest():
    a = 'abcd'
    b = [1,2]
    r = list(itertools.zip_longest(a,b, fillvalue='X'))
    print(r)

def run():
    infinite_interators()
    m_accumulate()
    m_chain()
    m_compress()
    m_filterfalse()
    m_zip_longest()


if __name__ == '__main__':
    run()
    print('done')
