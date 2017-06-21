a = 4
if(1 < a < 5):  # chained conditions
    print("1 < %s < 5" % (a))
# logical operators: and, or, not
if(a > 1 and a < 5):
    print("%s > 1 and %s < 5" % (a, a))

def printFibonacci(howMany=0):
    a, b = 1, 1
    print(a)
    howMany -= 1
    for count in range(0, howMany):
        a, b = b, a + b
        print(a)
# 1 1 2 3 5 8...
def printSomething(something='This is default'):
    print(something)
    
printFibonacci(6)
printSomething(something='using named parameters')
x = 10
y = 12
x, y = y, x * 2 # x = y(12), y = x(10) * 2, assignments are not done one after 
# the other the expressions on the right-hand side are all evaluated first 
# before any of the assignments take place. 
# The right-hand side expressions are evaluated from the left to the right.
print('x = %s, y = %s' % (x, y))
print('this','will','be','comma','separated')

a, b, c = [1,2,444]
print(a, b, c)
a, b = 9, 0
print(a, b)
