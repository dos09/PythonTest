import argparse

MEMORY_PROFILING = False
 
if MEMORY_PROFILING:
    from memory_profiler import profile
else:
    import builtins
 
    try:
        builtins.profile
    except AttributeError:
        # No line profiler, provide a pass-through version
        def profile(func):
            print('noop profile used')
            return func
 
        builtins.profile = profile

_100k = 100000
_1mil = 1000000
_5mil = 5000000
_50mil = 50000000


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

@profile
def t1():
    print('t1 start')
    a = [1] * (_50mil)
    print('t1 end')


@profile
def run(orc_name):
    print(orc_name)
    primes = get_primes(10)
    print(primes)
    t1()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--orc-name')
    args = parser.parse_args()
    run(args.orc_name)


"""
How to profile memory:
mprof run this_file_name.py
This will show memory usage (per line) for each @profile annotated function.
The "mprof run" creates a .dat file in the current directory and that file
can be used to show graph with:
mprof plot
The graph won't show which function was called, it will just show timeline
with RAM taken.
In order for the graph to show the function calls (only the @profile annotated)
must comment the "from memory_profiler import profile" and 
"mprof run this_file_name.py" + "mprof plot"

Scenario 1:
- want to profile and show line by line memory usage in console (graph
can show only timeline, no method calls)
set MEMORY_PROFILING to True and "mprof run t.py"
Scenario 2:
- want to profile and have the graph show method calls (no line by line
memory usage in the console output)
set MEMORY_PROFILING to False and "mprof run t.py", then "mprof plot"

Running the script, while MEMORY_PROFILE is True, will produce console output
similar to the one from Scenario 1 
"""
