import logging
from datetime import datetime
from time import asctime

# str = 'asd: dasd: gg:'
# a = str.split(':', 1)
# print(type(a[0]))

# str = '20170605T180907003'
# sd = str[0:8]
# print(sd)
# d = datetime.strptime(sd, '%Y%m%d').date()
# print(d)
# c = 2
# msg = 'This alert has been detected %s time%s on %s' % (c, c != 1 and 's' or '', d)
# evidence = """This alert has been detected 2 times on 2017-06-03
# This alert has been detected 2 times on 2017-06-02
# This alert has been detected 2 times on 2017-06-05
# """
# print(msg)
# print('is in evidence?', msg in evidence)

# class Orc:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp
#         #Orc.asd()
#         
#     def __str__(self):
#         return "%s - %s" % (self.name, self.hp)
#     
#     def __eq__(self,other):
#         return (self.name == other.name and
#                 self.hp == other.hp)
#     
#     def __hash__(self):
#         return hash((self.name, self.hp))
#     
#     @staticmethod
#     def asd():
#         print('stattttic')
#     
# def f1():
#     a = Orc('aaa', 100)
#     print(a.__hash__())
#     b = Orc('bbb', 200)
#     dup = Orc('aaa', 100)
#     print(dup.__hash__())
#     myset = set()
#     myset.add(a)
#     myset.add(b)
#     myset.add(dup)
#     for x in myset:
#         print(x)
#         
#     print(len(myset))

# log = logging.getLogger('orcs')
# log.addHandler(logging.StreamHandler())
# log.setLevel('DEBUG')
# log.debug('debug: %s %s %s', 'just', 'an', 'orc')
# log.info('info')
# log.warning('warning')
# log.error('error')
# log.critical('critical')
# 
# arr = ['a', 'b', 'c']
# 
# print('-'.join([i for i in arr]))

import re

    
def a(text):
    if text is None:
        text = ''
        
    text = re.sub(re.compile('\s{2,}'), ' ', text.strip())
    
    return text
    
print("'%s'" % a('     f     ff     '))
print("'%s'" % a(None))