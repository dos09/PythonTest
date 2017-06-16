# def gen1(nr):
#     cur = 0
#     while cur < nr:
#         cur += 1
#         yield cur
#          
#          
# for i in gen1(100):
#     print(i)

# not invoked on gen()

def gen():
    mylist = range(3)  # 0 1 2
    print('mylist: ', mylist)
    for i in mylist:
        print('gen\'s for loop')
        yield i * i

obj = gen()
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())

def f123():
    print('f123(): before one')
    yield 'f123(): yield one'
    print('f123(): after one')
    # after the first iteration the function is suspended here
    print('f123(): before two')
    yield 'f123():yield two'
    print('f123(): after two')
    # after the second iteration the function is suspended here
    print('f123(): before three')
    yield 'f123(): yield three'
    print('f123(): after three')
    # after the second iteration the function is suspended here
obj = f123()
print('before obj.__next__() 1')
obj.__next__()  # next() for Python 2
print('after obj.__next__() 1')

print('before obj.__next__() 2')
obj.__next__()
print('after obj.__next__() 2')

print('before obj.__next__() 3')
obj.__next__()
print('after obj.__next__() 3')