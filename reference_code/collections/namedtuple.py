from collections import namedtuple

Orc = namedtuple('Orc', 'name age kills'.split())

def _new_orc_1(**kvargs):    
    return Orc(kvargs.get('name'), 
               kvargs.get('age', None),
               kvargs.get('kills'))

def _new_orc_2(name, kills, age=None):
    return Orc(name, age, kills)

# dict = { name :'Ra', kills : 50 }
d = dict( name='Ra', kills=44 )

orc1 = _new_orc_1(name='Ra', kills=44)
orc2 = _new_orc_2('Asg', 50)

print(orc1)
print(orc1.name)
print(orc2)

# Point = namedtuple('Point', ['x', 'y'])
# Point = namedtuple('Point', 'x y')
Point = namedtuple('Point', 'x, y')
p = Point(11, y=22) # instantiate with positional or keyword arguments
print(p[0] + p[1]) # indexable like the plain tuple (11, 22)
print(p.x + p.y) # fields also accessible by name
a, b = p # unpack like a regular tuple
print(a, b)
print(p) # readable __repr__ with a name=value style
dict = {'x':10, 'y':20}
print(Point(**dict))
# print(p._source) # print the source for Point namedtuple
print('point fields:', p._fields)
od = p._asdict() # returns OrderedDict
print(od)
print(od['x'])