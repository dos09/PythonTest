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



def test_full():
    def m(a, b='B', c='C'):
        print(a,b,c)
    
    partial(m, 11, 12, 13)()
    partial(m, 21)()
    r = partial(m, 31, b=32)
    r()
    r(c=11111)

if __name__ == '__main__':
    test_full()
