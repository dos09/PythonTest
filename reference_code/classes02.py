#inheritance examples
class A():
    def __init__(self):
        self.value = 'vA'
        
    def get_id(self):
        return 'ID_A'

class B(A):
    def __init__(self):
        self.value = 'vB'
        
    def get_id(self):
        return 'ID_B'
        
class C(A):
    def __init__(self):
        self.value = 'vC'
        
    def get_id(self):
        return 'ID_C'
    
    def testC(self):
        print('testC:', A.get_id(self))
# https://en.wikipedia.org/wiki/Multiple_inheritance#The_diamond_problem
# diamond problem is resolved using the first base class' method/field
class D(B, C):
    pass

a = A()
b = B()
c = C()
d = D()

print(a.value, a.get_id(), type(a))
print(b.value, b.get_id(), type(b))
print(c.value, c.get_id(), type(c))
print(d.value, d.get_id(), type(d))

c.testC()