
def generate_XY():
    print('generate_XY')
    yield 'X'
    yield 'Y'

def run():
    generator = generate_XY()
    print('*')
    print(next(generator))
    print(next(generator))
    print(next(generator, 'EXHAUSTED'))
    
    generator = generate_XY()
    print('* *')
    for s in generator:
        print(s)
        
if __name__ == '__main__':
    run()