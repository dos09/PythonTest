from concurrent.futures import ThreadPoolExecutor
import threading

import psutil


def log(msg):
    print('(%s) %s' % (threading.get_ident(), msg))


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def check_prime_numbers(numbers):
    i = 0
    for num in numbers:
        if is_prime(num):
            pass
            # log('%s is prime' % num)
        i += 1
        if i % 200 == 0:
            log('CPU usage in %%: %s' %
                psutil.cpu_percent(interval=None, percpu=True))


def run():
    with ThreadPoolExecutor(max_workers=5) as pool:
        _from = 2
        _to = 10000
        numbers = [i for i in range(_from, _to)]
        slice_step = 1000
        for i in range(0, len(numbers), slice_step):
            numbers_slice = numbers[i:i + slice_step]
            pool.submit(check_prime_numbers, numbers_slice)

if __name__ == '__main__':
    run()
