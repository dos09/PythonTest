"""
How many IP-s I can keep in memory

LIMIT 5000000
(started) Memory used: 11.52 MB
(finished) Memory used: 449.82 MB
arr len: 5000000
"""

import psutil

LIMIT = 5000000


def show_mem(msg=None):
    r = psutil.Process().memory_info().rss / (1024 * 1024)
    r = round(r, 2)
    r = 'Memory used: %s MB' % r
    if msg:
        r = '(%s) %s' % (msg, r)

    print(r)


def gen_ips():

    def inc(p):
        v = s[p]
        if v == top_num:
            for i in range(p - 1, -1, -1):
                if s[i] != top_num:
                    s[i] += 1
                    p = i
                    break
            else:
                p = -1

            for i in range(p + 1, len(s)):
                s[i] = 0

            p = len(s) - 1
        else:
            s[p] += 1

        return p

    top_num = 255  # max IP = 255.255.255.255
    s = [top_num] * 4
    p = len(s) - 1
    for _ in range(LIMIT):
        p = inc(p)
        r = '.'.join(str(x) for x in s)
        yield r


def run():
    print('LIMIT', LIMIT)
    show_mem('started')
    arr = set()
    for ip in gen_ips():
        arr.add(ip)

    show_mem('finished')
    print('arr len:', len(arr))
    arr.add('banana')


if __name__ == '__main__':
    run()
