import asyncio
import random


@asyncio.coroutine
def print_num(num):
    print('print_num')
    for _ in range(5):
        print(num)
        yield from asyncio.sleep(random.uniform(0.5, 1.5))

    return num * 100


def run():
    event_loop = asyncio.get_event_loop()
    nums = (1, 2)
    coros = []
    for n in nums:
        coros.append(print_num(n))
    coros_results = event_loop.run_until_complete(asyncio.gather(*coros))
    event_loop.close()
    for num, res in zip(nums, coros_results):
        print('result for num %s: %s' % (num, res))

if __name__ == '__main__':
    run()
