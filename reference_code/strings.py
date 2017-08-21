# Strings
#########
print("String: %s, integer: %s, float: %s, string again: %s" 
      % ("something", 22, 3.4, 5 * "pet")) # pass arguments with tuple
multiStr = """this
is on
several
lines"""
print(multiStr)
# pass arguments with directory
print("%(key1)s and %(key2)s" % {"key1": "Gosho", "key2": "Misho"})
print("His name is {0}, he is {1} years"
      "old and weights '{2:7.2f}' kg".format("Django", 25, 100.1234))

str = 'army of orcs'
for c in str:
    print(c)
print('the first letter is \'%s\'' % (str[0]))
#Indices may also be negative numbers, to start counting from the right
print('the last letter is \'%s\'' % (str[-1]))
print('str len = %s' % (len(str)))
# str[inclusiveStartIndex : exclusiveEndIndex]
print('get a substring: \'%s\'' % (str[0:4]))
print('{:,}'.format(12412412))
print('{0:,}'.format(12412412))
s = "%s - %s" % ('tralala',200)  
print(s)

print("'%s'" % '12'.rjust(5))
print("'%s'" % '13'.ljust(5))
print("'%s'" % '14'.center(5))
print("'{0:5d}'".format(20))

print('This {orc} is bad'.format(orc='Mogka'))
print("int: '{0:5d}', float: '{1:.2f}'".format(4, 4.456))
# note the absence of 'f'
print("int: '{0:5}', float: '{1:.2}'".format(4, 4.456))
print("'%2.2f'" % 4.456)

orcs = {'mogka':1000, 'ra':1200}
print("orc's hps : {0[mogka]:d}, {0[ra]}".format(orcs))
print("orc's hps : {mogka:d}, {ra}".format(**orcs))

from sys import stdout

print('file=stdout is the default', file=stdout)
filename = 'temp_trash.log'
with open(filename, 'w') as f: 
    print(1,2,'aaa', file=f)
print('data was written to' ,filename)

print('"{:>5d}"'.format(123))
print('"{:<5d}"'.format(123)