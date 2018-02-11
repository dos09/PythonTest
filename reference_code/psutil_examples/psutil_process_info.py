import psutil

# can call this file from the terminal like (just for test):
# psutil_process_info.py -a banana    

def print_process_info():
    p = psutil.Process()  # can pass PID and see the info for specific process
    # improves fetching multiple process info
    with p.oneshot():
        print(' * Process name: %s' % p.name())
        print(' * Executable: %s' % p.exe())
        print(' * Current process status: %s' % p.status())
        print(' * Process current working directory: %s' % p.cwd())
        print(' * User owning the process: %s' % p.username())
        print(' * Memory info (rss): {:,} bytes'.format(p.memory_info().rss))
        print(' * Memory in percent (0 - 100): %.3f %%' %
              p.memory_percent(memtype="rss"))
        print(' * The command line this process has been called with: %s' %
              p.cmdline())


def run():
    limit = 5000000
    _ = [i for i in range(limit)]
    print_process_info()

if __name__ == '__main__':
    run()
