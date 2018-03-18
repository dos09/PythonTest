
def feed_me():
    data = yield 'X'
    print('received %s' % data)
    yield data

def run():
    generator = feed_me()
    print('*')
    print(next(generator))
    print('* *')
    print(generator.send('Y'))

if __name__ == '__main__':
    run()