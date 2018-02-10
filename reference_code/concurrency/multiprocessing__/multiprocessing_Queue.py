from multiprocessing import Process, Queue

def f(q):
    q.put([42, None, 'hello'])

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    # will block until there is something for reading from the queue
    print(q.get()) # prints "[42, None, 'hello']"
    p.join()