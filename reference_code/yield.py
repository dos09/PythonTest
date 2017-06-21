# not invoked on gen()
def gen():
    mylist = range(3)  # 0 1 2
    print('mylist: ', mylist)
    for i in mylist:
        print('gen\'s for loop')
        yield i * i
        
def f123():
    # suspended after returning the value of yield
    print('f123(): before one')
    yield 'f123(): yield one'
    
    print('f123(): after one')
    print('f123(): before two')
    yield 'f123(): yield two'
    
    print('f123(): after two')
    print('f123(): before three')
    yield 'f123(): yield three'
    
    print('f123(): after three')
    
            
print('use generator with "__next__"', '---------------------------')
obj = gen()
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print('use generator with "for x in getn()"', '---------------------------')
for x in gen():
    print(x)
print('use generator with "__next__"', '---------------------------')
obj = f123()
print('before obj.__next__() 1')
print(obj.__next__())  # next() for Python 2
print('after obj.__next__() 1')

print('before obj.__next__() 2')
print(obj.__next__())
print('after obj.__next__() 2')

print('before obj.__next__() 3')
print(obj.__next__())
print('after obj.__next__() 3')
# the last print from f123() is not executed
# if the generator is used like this:
# for x in f123(): print(x)
# the last print is executed
