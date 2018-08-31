import cProfile
import time

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def get_primes(limit=10):
    print('calculating primes below %s' % limit)
    primes = []
    for i in range(1, limit):
        if is_prime(i):
            primes.append(i)

    print('%s primes found below %s' % (len(primes), limit))
    return primes


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        msg = ('"%s" completed for %s' %
               (func.__name__,  round(time.time() - start_time, 2)))
        print(msg)
        return res

    return wrapper


@measure_time
def get_primes_measure():
    get_primes(20000)


def read_profile_stats():
    # https://docs.python.org/3/library/profile.html#pstats.Stats.print_stats
    import pstats
    p = pstats.Stats('out.txt')

    # sort by total time and print the first 10 entries
    p.sort_stats('tottime').print_stats(10)

    # print 20 %
    # p.sort_stats('tottime').print_stats(0.2)

    # order by total time and get first 10 lines containing prime
    # p.sort_stats('tottime').print_stats(10, 'prime')

if __name__ == '__main__':
    s = 'get_primes_measure()'
    # cProfile.run(s)
    # cProfile.run(s, filename='stats.txt') # TODO: check bad encoding
    get_primes_measure()
    # read_profile_stats()

"""
Can use cProfile from python script or from CLI.

- This will output statistics to out.txt. The data from out.txt can be manipulated
using the read_profile_stats (you have to use pstats.Stats class in order
to read the statistics)
python -m cProfile -o out.txt myprofiling.py
(can't use -s when -o is used)

- This will sort the output in console
python -m cProfile -s tottime myprofiling.py
(can't limit the number of results if using cProfile from CLI)


Example:
path_to/test_cProfile> python -m cProfile -s tottime myprofiling.py
calculating primes below 20000
2263 primes found below 20000
"get_primes_measure" completed for 2 sec.
         43347 function calls (42873 primitive calls) in 3.038 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    19999    2.954    0.000    2.954    0.000 calc_primes.py:1(is_prime)
     66/1    0.013    0.000    3.038    3.038 {built-in method builtins.exec}
      246    0.011    0.000    0.011    0.000 {built-in method nt.stat}
        5    0.008    0.002    0.008    0.002 {built-in method _imp.create_dynamic}
...
"""
