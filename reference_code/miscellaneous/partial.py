from functools import partial


def test01():
    def func(name, age):
        print('%s is %s years old' % (name, age))

    # partial(callable, *args, **kwargs)() = func(*args, **kwargs)
    p = partial(func, 'Asen', 20)
    p()
    p = partial(func, 'Ivan', age=21)
    p()


def test02():
    def print_a_b_c(a, b, c):
        print('a:', a)
        print('b:', b)
        print('c:', c)

    pass_b_only = partial(print_a_b_c, 'aaaaa', c='ccccc')
    pass_b_only('????')

if __name__ == '__main__':
    test02()
