from datetime import datetime

str = 'asd: bbb: gg:'
a = str.split(':', 1)
print(a)
print(type(a[0]), a[0])

str = '20170605T180907003'
sd = str[0:8]
print(sd)
d = datetime.strptime(sd, '%Y%m%d').date()
print(d)

c = 2
print('This alert has been detected %s time%s' % 
      (c, c != 1 and 's' or ''))

arr = ['a', 'b', 'c']
 
print('-'.join([i for i in arr]))
print('-'.join(arr))