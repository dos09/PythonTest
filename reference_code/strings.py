# Strings
#########
print("String: %s, integer: %s, float: %s, string again: %s" 
      % ("something", 22, 3.4, 5 * "pet")) # pass arguments with tuple
multiStr = """this
is on
several
lines"""
print(multiStr)
print("%(key1)s and %(key2)s" % {"key1": "Gosho", "key2": "Misho"}) # pass arguments with directory
print("His name is {0}, he is {1} years old and weights '{2:7.2f}' kg".format("Django", 25, 100.1234))

str = 'army of orcs'
for c in str:
    print(c)
print('the first letter is \'%s\'' % (str[0]))
#Indices may also be negative numbers, to start counting from the right
print('the last letter is \'%s\'' % (str[-1]))
print('str len = %s' % (len(str)))
print('get a substring: \'%s\'' % (str[0:4])) # str[inclusiveStartIndex : exclusiveEndIndex]
print('{:,}'.format(12412412))
print('{0:,}'.format(12412412))
s = "%s - %s" % ('tralala',200)  
print(s)
