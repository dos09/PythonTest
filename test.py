class A:
    def __init__(self):
        self.attr = {'edno':111, 'dve':222, 'tri':333}
    
    @property
    def edno(self):
        return self.attr.get('edno')
    
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
print(a.edno)

str = "I am {0:s} banana".format("yellow")
print(str)