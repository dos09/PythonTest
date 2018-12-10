import logging
import subprocess
import threading
import string
import random
import queue

LOG = logging.getLogger(__name__)


def get_random_string(slen):
    alnum_symbols = string.ascii_letters + string.digits
    return ''.join(random.choice(alnum_symbols) for _ in range(slen))


def gdb_stream_reader(stream, marker, q):
    c = 0  # TODO: remove
    marker_found = False
    stack_trace = []
    for line in stream:
        c += 1
        print('#%s %s' % (c, line), end='')

        if marker in line:
            if not marker_found:  # first time the marker is found
                marker_found = True
                LOG.debug('Marker found (first time)')
            else:
                LOG.debug('Marker found (second time)')
                break
        elif marker_found:  # this is the content between the two markers
            stack_trace.append(line)

    q.put(stack_trace)


def get_stack_trace(pid):
    """
    Get the stack trace of the process identified by <pid>
    """
    prog = subprocess.Popen(args=['sudo', 'gdb'],
                            shell=False,  # without intermediate process
                            bufsize=1,  # per line buffering
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            universal_newlines=True)
    q = queue.Queue(1)
    marker = get_random_string(100)
    t1 = threading.Thread(target=gdb_stream_reader,
                          args=(prog.stdout, marker, q))
    t1.start()
    prog.stdin.write('attach %s\n' % pid)
    prog.stdin.write('echo %s\n' % marker)
    # py-bt is extension command (not available with gdb only, need
    # python3-dbg)
    prog.stdin.write('py-bt\n')
    prog.stdin.write('echo %s\n' % marker)
    prog.stdin.write('detach\n')
    prog.stdin.write('quit\n')
    t1.join()
    return q.get()


if __name__ == '__main__':
    import argparse
    logging.basicConfig(level=logging.DEBUG)

    parser = argparse.ArgumentParser()
    parser.add_argument('pid', type=int,
                        help='Process for which to get the stack trace')
    pid = parser.parse_args().pid
    LOG.info('Using pid %s', pid)
    stack_trace = get_stack_trace(pid)
    print('Result:\n%s' % ''.join(line.lstrip() for line in stack_trace))
