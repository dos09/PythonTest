# Run concurrently in one thread

import asyncio
import threading

# asyncio is single-threaded, to run two tasks(coroutines) concurrently
# they must have await in order to give the event loop a chance to switch
# from the currently running coroutine to the other

# more info here:
# https://stackoverflow.com/questions/29269370/how-to-properly-create-and-run-concurrent-tasks-using-pythons-asyncio-module/29280606 


def log(msg):
    print('(%s) %s' % (threading.get_ident(), msg))


async def print_msg(msg, delay_seconds):
    log('print_msg, delay = %s' % delay_seconds)
    await asyncio.sleep(delay_seconds)
    log('msg: %s' % msg)
    # this is the result of the future object for the coroutine
    return delay_seconds


def test_simple_hello_world():
    event_loop = asyncio.get_event_loop()
    res = event_loop.run_until_complete(print_msg('hello world', 0.5))
    log('result: %s' % res)
    event_loop.close()


def test_simple_hello_world_2():
    event_loop = asyncio.get_event_loop()
    # the order of the results match the order in asyncio.gather
    results = event_loop.run_until_complete(
        asyncio.gather(print_msg('hello world 2 first', 0.7),
                       print_msg('hello world 2 second', 0.1)))
    log('results: %s' % results)
    event_loop.close()


def test_create_tasks():
    event_loop = asyncio.get_event_loop()
    task1 = event_loop.create_task(print_msg('first msg', 1))
    task2 = event_loop.create_task(print_msg('second msg', 0.5))
    tasks = []
    for t in (task1, task2):
        _task = asyncio.ensure_future(t)  # schedule for execution
        tasks.append(_task)

    # gather returns a future aggregating results from the
    # given coroutine objects or futures.
    future_obj = asyncio.gather(*tasks)
    res = event_loop.run_until_complete(future_obj)
    log('future_obj.result() %s' % future_obj.result())  # same as below
    log('res from run_until_complete' % res)  # same as above
    event_loop.close()

if __name__ == '__main__':
    # test_create_tasks()
    # test_simple_hello_world()
    test_simple_hello_world_2()
