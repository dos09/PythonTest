class A:
    def __init__(self):
        self._x = 0
        self.attr = {'edno':111, 'dve':222, 'tri':333}
    
    @property
    def edno(self):
        return self.attr.get('edno')
    
    @edno.setter
    def edno(self, value):
        self.attr['edno'] = value
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, x):
        if x < 0:
            x = 0
        elif x > 1000:
            x = 1000
        self._x = x
    
a = A()
print(a.x)
a.x = 12
print(a.x)
a.x = 1111
print(a.x)
a.x = -1
print(a.x)
print(a.edno)
a.edno = 300
print(a.edno)