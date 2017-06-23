# class A:
#     def __init__(self):
#         self.a = 'shrek'
# 
# obj = A()
# print(obj.a)
# print(getattr(obj, 'a'))
# try:
#     print(getattr(obj, 'b'))
# except AttributeError as ae:
#     print("getattr(obj, 'b') results in AttributeError:", ae)
# print(getattr(obj, 'b', 'donkey'))

# num = 1234567
# str = '{:,}'.format(num)
# print(type(str)) # <class 'str'>
# print(str) # 1,234,567

# print('failed ips ({:,}):'.format(4444, 1234))

d = {}
d.setdefault('a',1)
print(d['a'])