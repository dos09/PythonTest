# In Python 3.5 instead of using:
# - "@asyncio.coroutine" annotation to mark method as coroutine,
# can use "async def"
# - "yield from" to let the event loop execute other coroutines while waiting,
# can use "await"

import asyncio
import random


async def print_num(num):
    print('print_num')
    for _ in range(5):
        print(num)
        await asyncio.sleep(random.uniform(0.5, 1.5))

    return num * 1000


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
