from functools import partial

def func(name, age):
    print('%s is %s years old' % (name, age))

# partial(callable, *args, **kwargs)() = func(*args, **kwargs)
p = partial(func, 'Asen', 20)
p()
p = partial(func, 'Ivan', age=21)
p()