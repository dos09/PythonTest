import os
import sys
import time

import common

def run():
    if len(sys.argv) != 2:
        print('Must provide file to sort as argument')
        return
        
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print('%s is not a file' % filename)
        return
    
    sort_file(filename)

def sort_file(filename):
    print(' > Sorting %s' % filename)
    start_time = time.time()
    
    with open(filename) as f_in:
        items = [line for line in f_in]
        items.sort()
    
    filename = '%s_sorted' % filename
    with open(filename, 'w') as f_out:
        f_out.writelines('%s' % ''.join(items))
    
    print('Sorted result is in %s' % filename)
    seconds_elapsed = time.time() - start_time
    time_msg = ('Time elapsed %s (sorting %s)' %
                (common.format_time(seconds_elapsed), filename))
    print(time_msg)
    common.append_to_file('times', time_msg)
    return filename


if __name__ == '__main__':
    run()
    