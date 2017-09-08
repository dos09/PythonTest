import multiprocessing
from multiprocessing import Pool
from multiprocessing.sharedctypes import Array
import os
import time
from datetime import datetime

def _init(val):
    print('_init(): pid %s, received arg: %s' % 
          (os.getpid(), val))

def _callback(value):
    print('_callback(): pid %s' % (os.getpid()), end='')
    if isinstance(value, Exception):
        print(' Exception', value)
    else:
        print(' Work done: {0}'.format(value))
        
        
def _func(num):
    print('_func(): pid: %s' % os.getpid())
    time.sleep(0.3)
    print('_func(): pid: %s, num: %s' % (os.getpid(), num))

def test():
    print('test(): pid %s' % os.getpid())
    multiprocessing.set_start_method('spawn')
    procpool = Pool(
        5,
        initializer=_init,
        initargs=('tralala',)
    )
    
    for i in range(5):
        proc = procpool.apply_async(
            func=_func,
            args=[i],
            callback=_callback,
            error_callback=_callback
        )
        
    procpool.close()
    procpool.join()
    print('test finished')

# without the __main__ check the child processes will
# all execute test(), which leads to infinite recursion
if __name__ == '__main__':
    test()
    
# procpool.close() 
# Prevents any more tasks from being submitted to the pool. 
# Once all the tasks have been completed the worker processes will exit.