import concurrent.futures
 
import random
import time
 
def wait_and_print(delay_seconds):
    time.sleep(delay_seconds)
    print('Waited for %.2f seconds' % (delay_seconds))
 
def run():
    # the with statement will implicitly call pool.shutdown(wait=True)
    # which will wait for all of the currently started threads to finish
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        execution_count = 5
        for i in range(execution_count):
            delay_seconds = random.uniform(0.1, 1)
            pool.submit(wait_and_print, delay_seconds)
 
if __name__ == '__main__':
    run()
    print('done')
