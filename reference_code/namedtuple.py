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