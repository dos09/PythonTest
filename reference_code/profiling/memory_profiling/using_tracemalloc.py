"""
can start tracing memory by
tracemalloc.start()
or when starting the script

python -X tracemalloc x.py
(for linux should be python3)
"""

import tracemalloc

tracemalloc.start()

def run():
    print(tracemalloc.is_tracing())
    
    if tracemalloc.is_tracing():
        snapshot = tracemalloc.take_snapshot()
        top_stats = snapshot.statistics('lineno')
        for s in top_stats[:10]:
            print(s)

if __name__ == '__main__':
    run()

    