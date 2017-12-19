import os
import sys
import filecmp
import time

import common

def run():
    args = sys.argv
    if len(args) != 3:
        print('Invalid number of arguments')
        return
    
    f1_name = args[1]
    f2_name = args[2]
    cmp_files(f1_name, f2_name)

def cmp_files(f1_name, f2_name):
    assert f1_name != f2_name
    start_time = time.time()
    print(' > Comparing files (files must be sorted) %s, %s' % 
          (f1_name, f2_name))
    res = filecmp.cmp(f1_name, f2_name)
    print('%s equals %s ? : %s' % (f1_name, f2_name, res))
    seconds_elapsed = time.time() - start_time
    time_msg = ('Time elapsed %s (comparing %s and %s)' %
                (common.format_time(seconds_elapsed), f1_name, f2_name))
    print(time_msg)
    common.append_to_file('times', time_msg)
    return res

if __name__ == '__main__':
    run()