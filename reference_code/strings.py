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