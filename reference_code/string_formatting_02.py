import time
from datetime import datetime

LIMIT = 10000000


def time_elapsed(msg):
    def real_decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            res = func(*args, **kwargs)
            seconds_elapsed = round(time.time() - start_time, 2)
            print('%s (seconds elapsed %s)' % (msg, seconds_elapsed))
            return res

        return wrapper

    return real_decorator


@time_elapsed('OLD style formatting')
def test_old_style():
    s1 = 'dasdafijoiqjoidjoqidjfaadoir'
    s2 = '123980193'
    s3 = '#34809#)(8010310'
    for _ in range(LIMIT):
        s = '%s %s %s' % (s1, s2, s3)


@time_elapsed('NEW style formatting')
def test_new_style():
    s1 = 'dasdafijoiqjoidjoqidjfaadoir'
    s2 = '123980193'
    s3 = '#34809#)(8010310'
    for _ in range(LIMIT):
        s = '%s %s %s'.format(s1, s2, s3)

# the dashes are just for printing


def show_old_style():
    print('OLD style')
    print('-%+10s-' % 'banana')  # can skip the +
    print('-%-10s-' % 'banana')
    # no center alignment
    # can not choose the fill character
    print('-%.5s-' % 'truncated string')
    print('-%10.5s-' % 'truncated string')
    print('-%d-' % 4)
    print('-%f-' % 3.141592653589793)
    print('-%10d-' % 4)
    print('-%6.2f-' % 3.141592653589793)
    print('-%06.2f-' % 3.141592653589793)
    print('x%dx' % -4)
    print('x% dx' % -4)
    print('x% dx' % 4)  # the positive numbers are prefixed with space
    # can not control the position of the sign symbols
    d = {'name': 'Mogka', 'kills': 200}
    print('%(name)s %(kills)s' % d)


def show_new_style():
    print('\nNEW style')
    print('-{:>10}-'.format('banana'))
    print('-{:<10}-'.format('banana'))
    print('-{:^10}-'.format('bananaX'))  # center aligned
    print('-{:@<10}-'.format('banana'))  # choose fill character
    print('-{:.5}-'.format('truncated string'))
    print('-{:>10.5}-'.format('truncated string'))
    print('-{:d}-'.format(4))
    print('-{:f}-'.format(3.141592653589793))
    print('-{:>10d}-'.format(4))
    print('-{:6.2f}-'.format(3.141592653589793))
    print('-{:06.2f}-'.format(3.141592653589793))
    print('x{:d}x'.format(-4))
    print('x{: d}x'.format(-4))
    print('x{: d}x'.format(4))  # the positive numbers are prefixed with space
    # control the position of the sign symbols
    print('x{:=6d}x'.format(-6))  # note that the minus symbol if moved
    print('x{:=+6d}x'.format(6))  # to also show + sign for positive numbers
    d = {'name': 'Mogka', 'kills': 200}
    print('{name} {kills}'.format(**d))
    print('{name} {kills}'.format(name='Banana', kills=123))
    # with new style can access class' attributes and array's elements
    print('{orc[name]}'.format(orc=d))
    arr = [65, 43, 123, 15]
    print('{a[0]} {a[2]}'.format(a=arr))
    my_class = MyClass()
    print('{m.banana} {m.arr[0]}'.format(m=my_class))
    d = datetime.utcnow()
    print('{:%Y-%m-%d}'.format(d))
    print('-{:>{my_offset}}-'.format('banana', my_offset=10))


class MyClass():

    def __init__(self):
        self.banana = 'banana'
        self.arr = [{'n': 1}, {'n': 2}]


def test():
    # test_old_style()
    # test_new_style()
    show_old_style()
    show_new_style()


if __name__ == '__main__':
    test()
