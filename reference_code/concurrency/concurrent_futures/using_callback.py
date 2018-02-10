import concurrent.futures
import threading
import random
import time

def log(msg):
    print('(%s) %s' % (threading.get_ident(), msg))

def do_some_heavy_calculations(delay_seconds):
    time.sleep(delay_seconds)
    res = random.randint(1, 100)
    log('Worked for %.2f seconds' % delay_seconds)
    return res

# called when the future is done or cancelled
def callback(future_obj):
    res = future_obj.result()
    log('callback -> future\'s result: %s' % res)

def run():
    # the with statement will implicitly call pool.shutdown(wait=True)
    # which will wait for all of the currently started threads to finish
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        for _ in range(5):
            delay_seconds = random.uniform(0.1, 1)
            future_obj = pool.submit(do_some_heavy_calculations, 
                                     delay_seconds)
            future_obj.add_done_callback(callback)

if __name__ == '__main__':
    run()
    log('done')
