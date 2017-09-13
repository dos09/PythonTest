from operator import itemgetter
x = [4, 5, 3]

f = itemgetter(0) # = x[0]
print(f(x))

f = itemgetter(0, 1) # = (x[0], x[1])
print(f(x))
