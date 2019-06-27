import threading
import multiprocessing.dummy as m
import time


def p(msg):
    print('(%s) %s' % (threading.get_ident(), msg))


def w1():
    p('w1 method sleeping')
    time.sleep(4)
    return 'banana'


def w2():
    p('w2 method sleeping')
    time.sleep(2)
    raise Exception('mofooo')
    return 'mango'


def w3():
    p('w3 method sleeping')
    time.sleep(2)
    return 'papaya'


def run():
    funcs = [w1, w2, w3]
    arr = []
    with m.Pool(2) as pool:
        for func in funcs:
            r = pool.apply_async(func)
            arr.append(r)

        # in order to fail the whole program if Exception is raised in
        # any of the worker threads (otherwise it is ignored).
        # (If using the "error_callback" callback, it is handled in
        # separate thread so re-raising the exception makes the program hang)
        for r in arr:
            print(r.get())  # will fail when getting the result of w2

    print('run is done')


if __name__ == '__main__':
    run()
