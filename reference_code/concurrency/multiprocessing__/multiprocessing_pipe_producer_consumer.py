#from multiprocessing import Process, Pipe
import multiprocessing as mp

def consume(read_end):
    while True:
        try:
            data = read_end.recv()
            print(data)
        except EOFError:
            break

def produce(write_end):
    for i in range(5):
        write_end.send(i)

if __name__=='__main__':
    read_end, write_end = mp.Pipe(duplex=False)
    mp.set_start_method('spawn')
    reader = mp.Process(target=consume, args=(read_end,))
    reader.start()

    read_end.close()
    produce(write_end)
    write_end.close()
    reader.join()
    print('Exit')
