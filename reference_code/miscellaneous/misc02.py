# test dict.get() and getattr()

class A:
    def __init__(self):
        self.a = 'shrek'

obj = A()
print(obj.a)
print(getattr(obj, 'a'))
try:
    print(getattr(obj, 'b'))
except AttributeError as ae:
    print("getattr(obj, 'b') results in AttributeError:", ae)
print(getattr(obj, 'b', 'donkey'))

print('dict example:','------------------------------------')
dict = { 'a':4, 5:999 }
print('dict:', dict)
print("dict['a']:",dict['a'])

try:
    print(dict['b']) # KeyError
except KeyError:
    print("caught KeyError for dict['b']")
    
print("dict.get('b', 300):", dict.get('b', 300))
print("dict.get('b'):",dict.get('b'))