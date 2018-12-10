import subprocess
import threading
import string
import random
import queue

def get_random_string(slen):
    alnum_symbols = string.ascii_letters + string.digits
    return ''.join(random.choice(alnum_symbols) for _ in range(slen))


def stream_reader(stream, marker, q):
    c = 0
    for line in stream:
        c += 1
        print('#%s %s' % (c, line), end='')
        if marker in line:
            print('FOUND')
            q.put('FIRE')
            break


def run():
    """
    Write whatever you want using "write" (ALWAYS ADD \n at the end).
    A threat is reading the response.
    "write" some marker, when the threat finds the marker, it knows it should
    exit (or the rest to read is what we are interested in)
    """
    marker = get_random_string(100)
    q = queue.Queue(1)
    prog = subprocess.Popen(args='read_stdin2.py',
                            shell=True,
                            bufsize=1, # per line buffering
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            universal_newlines=True)
    t1 = threading.Thread(target=stream_reader, args=(prog.stdout, marker, q))
    t1.start()  # TODO check late start
    prog.stdin.write('banana\n')
    prog.stdin.write('banana2\n')
    prog.stdin.write('%s\n' % marker)
    
    print(q.get()) # wait for the threat
    t1.join()
    print('main done')


if __name__ == '__main__':
    run()


# <class '_io.TextIOWrapper'> <class '_io.TextIOWrapper'>
