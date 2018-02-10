from multiprocessing import Process, Lock
from random import randint
import time


def f(l, i):
    time.sleep(randint(1, 5) / 10)
    l.acquire()  # will block until it can acquire the lock
    try:
        print(i)
    finally:
        l.release()

if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start()

    print('main')
