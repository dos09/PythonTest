# Run concurrently in more than one thread

import asyncio
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from functools import partial

# asyncio is single-threaded, to run two tasks(coroutines) concurrently
# they must have await in order to give the event loop a chance to switch
# from the currently running coroutine to the other

# more info here:
# https://stackoverflow.com/questions/29269370/how-to-properly-create-and-run-concurrent-tasks-using-pythons-asyncio-module/29280606

# Note that print_msg is NOT coroutine

def log(msg):
    print('(%s) %s' % (threading.get_ident(), msg))


def print_msg(msg, delay_seconds):
    log('print_msg, delay = %s' % delay_seconds)
    time.sleep(delay_seconds)
    log('msg: %s' % msg)
    return delay_seconds


def run_in_executor():
    loop = asyncio.get_event_loop()
    executor = ThreadPoolExecutor(max_workers=5)
    # coro = coroutine object
    coros = []
    # run_in_executor starts the execution
    coros.append(loop.run_in_executor(executor, print_msg, 'one', 0.7))
    # if kwargs has to be used can use functools.partial
    coros.append(
        loop.run_in_executor(
            executor, partial(print_msg, msg='two', delay_seconds=0.1)
        )
    )
    # time.sleep(1)
    log('before run_until_complete')
    # "gather" returns future object which has for result list of the results 
    # of the coroutines in coros in the order they are appended to coros    
    results = loop.run_until_complete(asyncio.gather(*coros))
    log('results %s' % results)
    log('before executor shutdown')
    executor.shutdown() # wait for all threads to complete
    loop.close()

if __name__ == '__main__':
    run_in_executor()
    log('done')
