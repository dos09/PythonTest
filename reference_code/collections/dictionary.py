from collections import defaultdict, OrderedDict

mydictionary = {1: 3, "a": "valA", 44: "some"}
print("mydictionary: %s" % mydictionary)
print("mydictionary[\"a\"]: " + mydictionary["a"])

print('dictionary traversing:')
myd = {'a': 'letter a', 'b': 'letter b'}

for k, v in myd.items():
    print(k, v)

for k in myd:
    print(k, myd[k])

print('default/ordered dictionaries:')


class Orc:
    pass

d = {}
d.setdefault('a', 1)
print(d['a'])
# print(d['b']) # KeyError
d = defaultdict(Orc)  # default value must be callable
print(d['x'])  # insert key 'x' with value Orc()
print(d['y'])
print(d.get('z'))  # None, this makes no assignments

d1 = {'a': 9, 'b': 2}
d2 = {'a': 1, 'c': 3}
d1.update(d2)
print(d1)
print(d2)

od = OrderedDict()
od['b'] = 1
od['a'] = 2
od['c'] = 3
print(od)

print('ways to create dictionary:')

td = dict(one='A', two='B')
print('td', td)
print({'one': 'A', 'two': 'B'})
# dictionary comprehension
td = {x: x**2 for x in range(5)}
print(td)

d = {}
d[('a', 1)] = 'a-one'
d[('b', 2)] = 'b-two'
for (c, n), v in d.items():
    print(c, n, v)
    
d = {'a':1, 'b':2}
r = {k: v*10 for k, v in d.items()}
print(type(r), r)
