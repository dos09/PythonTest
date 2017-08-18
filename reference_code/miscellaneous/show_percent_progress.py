from random import randint
import time


def generate_number_array(size, lowest_value=0, highest_value=100):
    arr = []
    for i in range(0, size):
        arr.append(randint(lowest_value, highest_value))

    return arr


def show_progress_percent(arr):
    arr_len = len(arr)
    batch_limit = 1000
    processed = 0
    for i in range(0, arr_len):
        processed += 1
        if processed % batch_limit == 0 or processed == arr_len:
            percent = (processed * 100.) / arr_len
            print('processed:{0:7.2f} %'.format(percent))
            time.sleep(0.2)

arr = generate_number_array(size=13945)
show_progress_percent(arr)