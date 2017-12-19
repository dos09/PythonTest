import multiprocessing as mp
import os
import time
import random

def consumer(q):
    pid = os.getpid()
    
    while True:
        data = q.get()
        print('pid %s, data %s, type %s' % (pid, data, type(data)))
        time.sleep(random.uniform(0.2, 0.6))
        if data is None:
            q.put(data)
            break
            print('%s break' % pid)

if __name__ == '__main__':
    mp.set_start_method('spawn')
    q = mp.Queue()
    p1 = mp.Process(target=consumer, args=(q,))
    p2 = mp.Process(target=consumer, args=(q,))
    
    p1.start()
    p2.start()
    
    for i in range(10):
        q.put(i)
    
    q.put(None)
    p1.join()
    p2.join()
    print('Done')
    