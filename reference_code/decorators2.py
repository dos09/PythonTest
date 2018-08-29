def show_text(text):
    # decorator_with_args(arguments)(function)
    # so the decorator must return method taking the function and returning
    # callable wrapper
    print('show_text')

    def decorator(func):
        print('decorator')

        def wrapper(*args, **kwargs):
            print('warpper')
            print('argument text:', text)
            func(*args, **kwargs)

        return wrapper

    return decorator

# @measure_time(name='M!!!!!')
# @hello
@show_text('ASD') # this must return the real decorator taking function as arg
def m1(banana=None):
    print('m1', banana)


def run():
    m1('banana')

if __name__ == '__main__':
    run()